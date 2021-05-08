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


async def get_from(message: types.Message):
    return await sync_to_async(Profile.objects.get, thread_sensitive=True)(external_id=message.from_user.id)


async def not_started(message: types.Message):
    text = 'Я не знаю, что на это ответить :( \n\nПомощь - /help '
    patterns = ['нача', 'начн', 'продолж' 'старт', 'привет', 'здравст', 'салам']
    kb = None
    counter = 0
    for p in patterns:
        if p in message.text.lower() and counter == 0:
            counter += 1
            text = ''
            if p in patterns[-3:-1]:
                text = 'Привет, хочешь начать игру? \n'
            title = '"ВЕДЬМАК: ТРОЛЛЬЯ ВЕНДЕТТА"'
            main_title = f'\n{title}\n'
            profile = await get_from(message)

            kb = game_not_exist_kb
            resume = ''
            if profile.position != 1:
                resume = 'или продолжите текущую'
                kb = game_exist_kb
            text += f'{main_title}\n'
            text += f'Начните новую игру {resume}!'
    patterns = ['таблиц', 'спис', 'лидер', 'рейтинг']
    counter = 0
    for p in patterns:
        if p in message.text.lower() and counter == 0:
            counter += 1
            if 'не знаю' in text:
                text = 'Вы можете ознакомиться с таблицей лидеров на сайте:'
            else:
                text += '\n\nВы также можете ознакомиться с таблицей лидеров'
            if kb:
                kb.add(website_button)
            else:
                kb = InlineKeyboardMarkup().add(website_button)

    await message.answer(text) if not kb else await message.answer(text, reply_markup=kb)


async def started(message: types.Message, session):
    text, image, sticker, kb = session.message_process(message)

    if sticker:
        await message.answer_sticker(sticker)

    await message.answer(text)


states = {
    'not_started': not_started,
    'started': started,
}


# rpg = Session(rpg_data=rpg_data)
@dp.callback_query_handler(lambda c: c.data == 'start_game')
async def process_callback_start_game(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    p = await sync_to_async(Profile.objects.get)(external_id=callback_query.from_user.id)
    session = Session(profile=p, new=True)

    loop = asyncio.get_running_loop()
    loop.create_task(session.scheduled())

    sessions[callback_query.from_user.id] = session
    p.state = 'started'
    await sync_to_async(p.save)()
    await bot.send_message(callback_query.from_user.id, 'Игра начинается!')


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
    # TODO сделать диалог: вы точно хотите выйти?

    await states['not_started'](message)


@dp.message_handler(commands=['leaders'])
async def process_leaders_command(message: types.Message):
    message.text = 'таблица'
    await states['not_started'](message)


@dp.message_handler()
async def base_handler(message: types.Message):
    if not sessions[message.from_user.id]:
        await states['not_started'](message)
    else:
        session = sessions[message.from_user.id]
        await states[session.profile.state](message, session)


class Command(BaseCommand):
    help = 'Бот'

    def handle(self, *args, **kwargs):
        executor.start_polling(dp, skip_updates=True)

