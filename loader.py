from aiogram import Bot, Dispatcher

from amplitude import Amplitude

from config import BOT_TOKEN, AMPLITUDE_API_KEY

import logging

logging.basicConfig(level=logging.INFO)


bot = Bot(BOT_TOKEN, parse_mode="HTML")

dp = Dispatcher(bot)

amplitude = Amplitude(AMPLITUDE_API_KEY)
