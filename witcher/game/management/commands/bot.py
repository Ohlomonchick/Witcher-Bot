import asyncio

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

def start():
    pass


states = {
    'start': start,
}


# rpg = Session(rpg_data=rpg_data)
@dp.callback_query_handler(lambda c: c.data == 'start_game')
async def process_callback_start_game(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    p = await sync_to_async(Profile.objects.get)(external_id=callback_query.from_user.id)
    session = Session(profile=p)

    loop = asyncio.get_running_loop()
    loop.create_task(session.scheduled())

    sessions[callback_query.from_user.id] = session
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


class Command(BaseCommand):
    help = 'Бот'

    def handle(self, *args, **kwargs):
        executor.start_polling(dp, skip_updates=True)

