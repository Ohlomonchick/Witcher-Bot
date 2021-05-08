from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

start_game = InlineKeyboardButton('Новая Игра', callback_data='start_game')
resume_game = InlineKeyboardButton('Продолжить Игру', callback_data='resume_game')

website_button = InlineKeyboardButton('Таблица Лидеров', url='https://vk.com/ohlomonchick337')

game_exist_kb = InlineKeyboardMarkup(row_width=2).add(start_game)
game_exist_kb.add(resume_game)

game_not_exist_kb = InlineKeyboardMarkup().add(start_game)