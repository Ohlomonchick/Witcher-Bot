import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.markdown import text
from asgiref.sync import sync_to_async
from django.core.management.base import BaseCommand
from django.core.files import File

from .config import TOKEN
from .keyboards import *
from .session import Session
from ...models import Profile

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

log = logging.getLogger()

sessions = {}


async def get_session(message=None, user_id=None, chosen=None):
    if message:
        user_id = message.from_user.id
    if user_id in sessions.keys():
        return sessions[user_id]
    else:
        p = await sync_to_async(Profile.objects.get)(external_id=user_id)
        if p.state == 'not_started':
            await not_started(message)
        else:
            session = Session(profile=p, new=False)
            loop = asyncio.get_running_loop()
            loop.create_task(session.scheduled())

            sessions[user_id] = session
            return session


async def get_from_db(message):
    if type(message) == int:
        return await sync_to_async(Profile.objects.get, thread_sensitive=True)(external_id=message)
    else:
        return await sync_to_async(Profile.objects.get, thread_sensitive=True)(external_id=message.from_user.id)


async def not_started(message: types.Message):
    answer_text = 'Я не знаю, что на это ответить :( \n\nПомощь - /help '
    patterns = ['нача', 'начн', 'игра', 'продолж', 'старт', 'привет', 'здравст', 'салам', 'рекорд', 'результат']
    kb = None
    profile = None
    counter = 0
    for p in patterns[:-2]:
        if p in message.text.lower() and counter == 0:
            counter += 1
            answer_text = ''
            if p in patterns[-5:-3]:
                answer_text = 'Привет, хочешь начать игру? \n'
            title = '"ВЕДЬМАК: ТРОЛЛЬЯ ВЕНДЕТТА"'
            main_title = f'\n{title}\n'
            profile = await get_from_db(message)

            kb = game_not_exist_kb
            resume = ''
            if profile.position != 1:
                resume = 'или продолжите текущую'
                kb = game_exist_kb
            answer_text += f'{main_title}\n'
            answer_text += f'Начните новую игру {resume}!'
    counter = 0
    for p in patterns[-2:-1]:
        if p in message.text.lower() and counter == 0:
            if not profile:
                profile = await get_from_db(message)
            your_goal = f'\n\nВАШ РЕКОРД:   {profile.total}\n'
            if 'не знаю' in answer_text:
                answer_text = your_goal
            else:
                answer_text += your_goal

    kb, answer_text = await table(0, kb, message, answer_text)

    await message.answer(answer_text) if not kb else await message.answer(answer_text, reply_markup=kb)


async def table(counter, kb, message, text):
    patterns = ['таблиц', 'спис', 'лидер', 'рейтинг']
    for p in patterns:
        if p in message.text.lower() and counter == 0:
            counter += 1
            if 'не знаю' in text:
                text = 'Вы можете ознакомиться с таблицей лидеров на сайте:'
            else:
                text += '\nВы также можете ознакомиться с таблицей лидеров'
            if kb and kb == game_exist_kb:
                kb = InlineKeyboardMarkup(row_width=2).add(start_game).insert(resume_game).add(website_button)
            elif kb and kb == game_not_exist_kb:
                kb = InlineKeyboardMarkup().add(start_game).add(website_button)
            else:
                kb = InlineKeyboardMarkup().add(website_button)
    return kb, text


async def started(message: types.Message, session: Session):
    text, image, sticker, kb = await session.action_process(message)
    if text == '':
        text = 'Я не знаю, как на это ответить\nПомощь - /help'

    kb, text = await table(0, kb, message, text)

    if sticker:
        await message.answer_sticker(sticker)
    if kb:
        await message.answer(text, reply_markup=kb)
    else:
        await message.answer(text)


async def wrong_answer(message: types.Message, session: Session):
    if session.profile.state != 'wrong_answer':
        message.text = ''
        await states[session.profile.state](message)
    else:
        session.action_data = session.rpg_data[session.profile.position - 1]
        session.answer = session.action_data['answer']
        response = await session.answer_check(message)
        if response:
            session.chosen_action = response[0]
            await message.answer(response[1])
            message.text = ''
            await started(message, session)


states = {
    'not_started': not_started,
    'started': started,
    'wrong_answer': wrong_answer,
}


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn'))
async def process_callback_btn(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    place = int(callback_query.data[callback_query.data.index('_') + 1:-2])

    user_id = callback_query.from_user.id
    if user_id in sessions.keys():
        session = sessions[user_id]
    else:
        session = await get_session(user_id=user_id)
        session.available_actions = [context for context, i in session.action_data['actions'].items()
                                     if (i[1] is None or session.profile.achievement[i[1]])]

    if place == int(session.action_data['name']):
        await bot.answer_callback_query(callback_query.id)
        session.chosen_action = int(code)

        answer_text, image, sticker, kb = await session.action_process()
        if sticker:
            await bot.send_sticker(user_id, sticker)
        if kb:
            if image:
                try:
                    await bot.send_photo(user_id, image, reply_markup=kb, caption=answer_text)
                except Exception as exc:
                    await bot.send_photo(user_id, image)
                    await bot.send_message(user_id, answer_text, reply_markup=kb)
            else:
                await bot.send_message(user_id, answer_text, reply_markup=kb)
        else:
            await bot.send_message(user_id, answer_text)
    else:
        await bot.answer_callback_query(callback_query.id, text='Не та часть истории!', show_alert=True)


async def process_start(callback_query, new):
    user_id = callback_query.from_user.id
    if user_id in sessions.keys() and sessions[user_id].profile.state == 'started':
        await bot.send_message(user_id, 'Вы уже начали игру\n\nСохранить и выйти - /quit')
        return

    if user_id in sessions.keys():
        session = Session(profile=sessions[user_id].profile, new=new[1], data=sessions[user_id].rpg_data)
        session.profile.state = 'started'
        sessions[user_id] = session

        await sync_to_async(session.profile.save)()
    else:
        p = await sync_to_async(Profile.objects.get)(external_id=user_id)
        session = Session(profile=p, new=new[1])
        p.state = 'started'
        loop = asyncio.get_running_loop()
        loop.create_task(session.scheduled())
        sessions[user_id] = session

        await sync_to_async(p.save, thread_sensitive=False)()
    await bot.send_message(user_id, new[0])

    answer_text, image, sticker, kb = await session.action_process()
    if sticker:
        await bot.send_sticker(user_id, sticker)
    if image:
        await bot.send_photo(user_id, image)
    if kb:
        await bot.send_message(user_id, answer_text, reply_markup=kb)
    else:
        await bot.send_message(user_id, answer_text)


@dp.callback_query_handler(lambda c: c.data == 'start_game')
async def process_callback_start_game(callback_query: types.CallbackQuery):
    new = ('Игра начинается', True)
    await bot.answer_callback_query(callback_query.id)
    await process_start(callback_query, new=('Игра начинается!', True))


@dp.callback_query_handler(lambda c: c.data == 'resume_game')
async def process_callback_resume_game(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await process_start(callback_query, new=('Игра продолжается!', False))


@dp.callback_query_handler(lambda c: c.data == 'quit_game')
async def process_callback_start_game(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    await bot.answer_callback_query(callback_query.id)

    session = await get_session(user_id=user_id)
    if session.profile.state == 'not_started':
        await bot.send_message(user_id, "Вы и так не в игре")
    else:
        session.profile.state = 'not_started'
        await sync_to_async(session.profile.save)()
        session.can_be_deleted = True
        session.appeals = 0
        await bot.send_message(user_id, "Игра сохранена")

        title = '"ВЕДЬМАК: ТРОЛЛЬЯ ВЕНДЕТТА"'
        main_title = f'\n{title}\n'
        profile = await get_from_db(callback_query.from_user.id)

        kb = game_not_exist_kb
        resume = ''
        if profile.position != 1:
            resume = 'или продолжите текущую'
            kb = game_exist_kb
        answer_text = f'{main_title}\n'
        answer_text += f'Начните новую игру {resume}!'
        answer_text += f'\n\nВАШ РЕКОРД: {profile.total}'

        answer_text += '\n\nВы также можете ознакомиться с таблицей лидеров'
        if kb == game_exist_kb:
            kb = InlineKeyboardMarkup().add(start_game).add(resume_game).add(website_button)
        else:
            kb = InlineKeyboardMarkup().add(start_game).add(website_button)

        await bot.send_message(user_id, answer_text, reply_markup=kb)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    text = f''
    defaults = {
        'name': message.from_user.username,
    }
    p, created = await sync_to_async(Profile.objects.get_or_create, thread_sensitive=True)(
        external_id=message.from_user.id,
        defaults=defaults
    )
    if created or not p.photo:
        got_photos = await bot.get_user_profile_photos(message.from_user.id)
        if got_photos.total_count > 0:
            try:
                photo = got_photos.photos[0][0]["file_id"]
                file_info = await bot.get_file(photo)
                downloaded = await bot.download_file(file_info.file_path)
                src = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..', 'game/media/photos'))
                new_path = file_info.file_path[file_info.file_path.index('/') + 1:]
                src = os.path.join(src, new_path)

                await sync_to_async(p.photo.save)(new_path, File(downloaded), save=True)
            except Exception as exc:
                print(exc)

    kb = game_not_exist_kb
    title = 'ДОБРО ПОЖАЛОВАТЬ В ИГРУ "ВЕДЬМАК: ТРОЛЛЬЯ ВЕНДЕТТА"'
    main_title = f'\n{title}\n'
    disclaimer = '\nDISCLAIMER:\nИгра сохраняется автоматически после минуты бездействия, \n'
    disclaimer += 'но вы также можете сохранять её вручную.\n Максимальное количество очков,\n'
    disclaimer += 'когда либо набранное вами, не сбрасывается после начала новой игры.\nУдачной игры!\n'
    if created:
        text += f'{main_title}{disclaimer}\n\nТаблица лидеров:'
    else:
        resume = ''
        if p.position != 1:
            resume = 'или продолжите текущую'
            kb = game_exist_kb
        text += f'{main_title}{disclaimer}Рад снова тебя видеть.\n\nВАШ РЕКОРД:   {p.total}'
        text += f'\n\nНачните новую игру {resume}!'
    kb.add(website_button)
    image = 'AgACAgIAAxkBAAMIYJmUP9UZseeI_vU2fq2YfkIC1LgAAmqzMRvr2dFIEwg1XWuk_pjVSzSfLgADAQADAgADbQADJdQDAAEfBA'
    await bot.send_photo(message.from_user.id, image, reply_markup=kb, caption=text)


help_message = text(
    "Доступные команды:\n",
    "/start - приветствие",
    "/game - главное меню игры",
    "/leaders - список лидеров",
    "/goal - ваш рекорд",
    "\nВы также можете просто попросить бота",
    "выполнить какое-либо действие",
    sep="\n"
)


@dp.message_handler(commands=['help'])
async def process_help_message(message: types.Message):
    await message.answer(help_message)


@dp.message_handler(commands=['game'])
async def process_game_command(message: types.Message):
    message.text = 'начало таблица рекорд'
    await states['not_started'](message)


@dp.message_handler(commands=['leaders'])
async def process_leaders_command(message: types.Message):
    message.text = 'таблица'
    await states['not_started'](message)


@dp.message_handler(commands=['goal'])
async def process_leaders_command(message: types.Message):
    message.text = 'рекорд'
    await states['not_started'](message)


@dp.message_handler(commands=['quit'])
async def process_quit_command(message: types.Message):
    session = await get_session(message=message)
    if session.profile.state == 'not_started':
        await message.answer("Вы и так не в игре")
    else:
        session.profile.state = 'not_started'
        await sync_to_async(session.profile.save)()
        session.can_be_deleted = True
        session.appeals = 0
        await message.answer("Игра сохранена")
        message.text = 'Начать таблица продолжить'
        await states['not_started'](message)


@dp.message_handler(content_types=['photo'])
async def scan_message(message: types.Message):
    await message.answer('Я не знаю, как на это ответить\nПомощь - /help')


@dp.message_handler(content_types=['audio'])
async def scan_message(message: types.Message):
    await message.answer('Я не знаю, как на это ответить\nПомощь - /help')


@dp.message_handler()
async def base_handler(message: types.Message):
    session = await get_session(message)
    if session:
        session.can_be_deleted = False
        if session.profile.state != 'not_started':
            await states[session.profile.state](message, session)


async def garbage_collector(wait_for):
    while True:
        await asyncio.sleep(wait_for)
        keys_to_collect = []
        for key, value in sessions.items():
            if value.can_be_deleted:
                keys_to_collect.append(key)
                log.info(f'Удалена Сессия {value.profile.name}')
        for key in keys_to_collect:
            sessions.pop(key)


class Command(BaseCommand):
    help = 'Бот'

    def handle(self, *args, **kwargs):
        try:
            loop = asyncio.get_event_loop()
            loop.create_task(garbage_collector(600))
            executor.start_polling(dp, skip_updates=True)
        except Exception as exc:
            print(exc)
            self.handle(*args, **kwargs)
