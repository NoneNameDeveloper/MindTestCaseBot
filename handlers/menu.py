from aiogram import types

from engine.utils import process_menu


from loader import dp


@dp.message_handler(commands=['menu'], chat_type='private')
async def start_message(message: types.Message):
	await process_menu(message)
