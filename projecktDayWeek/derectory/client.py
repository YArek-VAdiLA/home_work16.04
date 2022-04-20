from aiogram import Dispatcher, types
from key_bord import kb_day


async def send_welcome(message: types.Message):
    await message.reply("Hello!", reply_markup=kb_day)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['hello'])