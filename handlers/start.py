from sqlalchemy import select, insert

from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from engine.db_api.base import get_session
from engine.utils import amplitude_log, process_start

from engine.db_api import Users, Settings

from loader import dp


@dp.message_handler(CommandStart(), chat_type='private')
async def start_message(message: types.Message):
	await process_start(message)
