from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton

button_start = KeyboardButton('/start')

kb_day = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_day.add(button_start)


button_cancel = KeyboardButton('/cancel')

kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cancel.add(button_cancel)


