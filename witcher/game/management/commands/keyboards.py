from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_game = InlineKeyboardButton('Новая Игра', callback_data='start_game')
resume_game = InlineKeyboardButton('Продолжить Игру', callback_data='resume_game')

website_button = InlineKeyboardButton('Таблица Лидеров', url='http://dimonchick.pythonanywhere.com/')

game_exist_kb = InlineKeyboardMarkup(row_width=2).add(start_game)
game_exist_kb.insert(resume_game)

game_not_exist_kb = InlineKeyboardMarkup().add(start_game)