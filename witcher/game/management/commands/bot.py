import asyncio

from aiogram.utils.markdown import text
from asgiref.sync import sync_to_async

from .config import TOKEN
import logging
from .keyboards import *
from .game_data import rpg_data

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from django.core.management.base import BaseCommand

from ...models import Profile
from .session import Session

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

log = logging.getLogger()

sessions = {}


def log_errors(f):
    def inner(*args, **kwargs):
        try:
            f(*args, **kwargs)
        except Exception as exc:
            error_message = f'\nПРОИЗОШЛА ОШИБКА:   {exc}'
            log.info(error_message)

    return inner


async def get_session(message=None, user_id=None, chosen=None):
    if message:
        user_id = message.from_user.id
    if user_id in sessions.keys():
        return sessions[user_id]
    else:
        p = await sync_to_async(Profile.objects.get)(external_id=user_id)
        if p.state == 'not_started':
            # TODO сделать вызов not_started для кнопок
            # message.text = 'Старт продолжить таблица'
            await not_started(message)
        else:
            session = Session(profile=p, new=False)

            loop = asyncio.get_running_loop()
            loop.create_task(session.scheduled())

            sessions[user_id] = session

            return session


async def get_from(message):
    if type(message) == int:
        return await sync_to_async(Profile.objects.get, thread_sensitive=True)(external_id=message)
    else:
        return await sync_to_async(Profile.objects.get, thread_sensitive=True)(external_id=message.from_user.id)


async def not_started(message: types.Message):
    answer_text = 'Я не знаю, что на это ответить :( \n\nПомощь - /help '
    patterns = ['нача', 'начн', 'продолж', 'старт', 'привет', 'здравст', 'салам']
    kb = None
    counter = 0
    for p in patterns:
        if p in message.text.lower() and counter == 0:
            counter += 1
            answer_text = ''
            if p in patterns[-3:-1]:
                answer_text = 'Привет, хочешь начать игру? \n'
            title = '"ВЕДЬМАК: ТРОЛЛЬЯ ВЕНДЕТТА"'
            main_title = f'\n{title}\n'
            profile = await get_from(message)

            kb = game_not_exist_kb
            resume = ''
            if profile.position != 1:
                resume = 'или продолжите текущую'
                kb = game_exist_kb
            answer_text += f'{main_title}\n'
            answer_text += f'Начните новую игру {resume}!'
    counter = 0
    kb, answer_text = await table(counter, kb, message, answer_text)

    await message.answer(answer_text) if not kb else await message.answer(answer_text, reply_markup=kb)


async def table(counter, kb, message, text):
    patterns = ['таблиц', 'спис', 'лидер', 'рейтинг']
    for p in patterns:
        if p in message.text.lower() and counter == 0:
            counter += 1
            if 'не знаю' in text:
                text = 'Вы можете ознакомиться с таблицей лидеров на сайте:'
            else:
                text += '\n\nВы также можете ознакомиться с таблицей лидеров'
            if kb and kb == game_exist_kb:
                kb = InlineKeyboardMarkup().add(start_game).add(resume_game).add(website_button)
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
        response = await session._answer_check(message)
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


# TODO сделать проверку на уникальность
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn'))
async def process_callback_btn(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    user_id = callback_query.from_user.id
    if user_id in sessions.keys():
        session = sessions[user_id]
    else:
        session = await get_session(user_id=user_id)
        session.available_actions = [context for context, i in session.action_data['actions'].items()
                                      if (i[1] is None or session.profile.achievement[i[1]])]

    session.chosen_action = int(code)

    answer_text, image, sticker, kb = await session.action_process()

    if sticker:
        await bot.send_sticker(user_id, sticker)

    if kb:
        await bot.send_message(user_id, answer_text, reply_markup=kb)
    else:
        await bot.send_message(user_id, answer_text)


async def process_start(callback_query, new):
    user_id = callback_query.from_user.id
    if user_id in sessions.keys() and sessions[user_id].profile.state == 'started':
        await bot.send_message(user_id, 'Вы уже начали игру\n\nСохранить и выйти - /quit')
        return
    p = await sync_to_async(Profile.objects.get)(external_id=user_id)
    session = Session(profile=p, new=new[1])

    loop = asyncio.get_running_loop()
    loop.create_task(session.scheduled())

    sessions[user_id] = session
    p.state = 'started'
    await sync_to_async(p.save)()
    await bot.send_message(user_id, new[0])

    answer_text, image, sticker, kb = await session.action_process()

    if sticker:
        await bot.send_sticker(user_id, sticker)

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
    await process_start(callback_query, new=('Игра продолжается!', False))


@dp.callback_query_handler(lambda c: c.data == 'quit_game')
async def process_callback_start_game(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id

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
        profile = await get_from(callback_query.from_user.id)

        kb = game_not_exist_kb
        resume = ''
        if profile.position != 1:
            resume = 'или продолжите текущую'
            kb = game_exist_kb
        answer_text = f'{main_title}\n'
        answer_text += f'Начните новую игру {resume}!'

        answer_text += '\n\nВы также можете ознакомиться с таблицей лидеров'
        if kb == game_exist_kb:
            kb = InlineKeyboardMarkup().add(start_game).add(resume_game).add(website_button)
        else:
            kb = InlineKeyboardMarkup().add(start_game).add(website_button)

        await bot.send_message(user_id, answer_text, reply_markup=kb)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    text = f'Ваш id: {message.from_user.id} \n'

    p, created = await sync_to_async(Profile.objects.get_or_create, thread_sensitive=True)(
        external_id=message.from_user.id,
        defaults={
            'name': message.from_user.username,
        }
    )
    text += str(p.achievement)
    kb = game_not_exist_kb
    title = 'ДОБРО ПОЖАЛОВАТЬ В ИГРУ "ВЕДЬМАК: ТРОЛЛЬЯ ВЕНДЕТТА"'
    main_title = f'\n{title}\n'
    if created:
        text += f'{main_title}\n\nТаблица лидеров:'
    else:
        resume = ''
        if p.position != 1:
            resume = 'или продолжите текущую'
            kb = game_exist_kb
        text += f'{main_title}\nДавно не виделись...\n\nТаблица лидеров:'
        text += f'\n\nНачните новую игру {resume}!'

    await message.answer_sticker(r'CAACAgIAAxkBAAEBREJglW1P_KkgG9GqO8ooNrKz4s3ZpwACKwYAAtJaiAHsejwtswOtzR8E')
    await message.answer(text + '\n' + str(created), reply_markup=kb)


help_message = text(
    "Это урок по клавиатурам.",
    "Доступные команды:\n",
    "/start - приветствие",
    "/game - главное меню игры",
    "/leaders - список лидеров",
    "\nВы также можете просто попросить бота",
    "выполнить какое-либо действие",
    sep="\n"
)


@dp.message_handler(commands=['help'])
async def process_help_message(message: types.Message):
    await message.answer(help_message)


@dp.message_handler(commands=['game'])
async def process_game_command(message: types.Message):
    message.text = 'начало таблица'
    await states['not_started'](message)


@dp.message_handler(commands=['leaders'])
async def process_leaders_command(message: types.Message):
    message.text = 'таблица'
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
        # try:
        loop = asyncio.get_event_loop()
        loop.create_task(garbage_collector(50))
        executor.start_polling(dp, skip_updates=True)
        # except Exception as exc:
        #     print(exc)
        #     self.handle(*args, **kwargs)
