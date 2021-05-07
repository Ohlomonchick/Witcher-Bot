from asgiref.sync import sync_to_async

from .config import TOKEN
import logging
import time
# import asyncio
# from datetime import datetime
from .rpg_data import rpg_data

from aiogram import Bot, Dispatcher, executor, types
from django.core.management.base import BaseCommand

from ...models import Profile

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

log = logging.getLogger()


def time_track(f):

    def inner(*args, **kwargs):
        started_at = time.time()

        f(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
    return inner


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


class RPG:

    def __init__(self, rpg_data, state):
        # global rpg_data
        self.rpg_data = rpg_data
        self.action_data = self.rpg_data[0]
        self.action = self.action_data['name']
        self.chosen_action = None
        self.available_actions = None
        self.message = ''
        self.started = False
        self.answer = None
        self.state = None

    def

rpg = RPG(rpg_data=rpg_data)

@dp.message_handler()
async def base_message_handler(message: types.Message)
    global rpg
    started_at = time.time()

    text = f'Ваш id: {message.from_user.id} \n \nТекст: '

    p, _ = await sync_to_async(Profile.objects.get_or_create, thread_sensitive=True)(
        external_id=message.from_user.id,
        defaults={
            'name': message.from_user.username,
        }
    )
    if _ == True:

    await message.answer(text + message.text + '\n' + str(_))

    ended_at = time.time()
    elapsed = round(ended_at - started_at, 4)
    print(f'Функция работала {elapsed} секунд(ы)')


# run longpolling
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)

class Command(BaseCommand):
    help = 'Бот'

    def handle(self, *args, **kwargs):
        executor.start_polling(dp, skip_updates=True)

