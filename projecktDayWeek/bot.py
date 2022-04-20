import logging
from aiogram import executor
from create_bot import dp
from derectory import bot_def
from derectory import register_handlers

logging.basicConfig(level=logging.INFO)

bot_def.register_hendlers(dp)
register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

