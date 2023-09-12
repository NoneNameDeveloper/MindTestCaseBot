from aiogram import types

from engine.service import set_character, get_settings
from engine.utils import amplitude_log
from loader import dp


@dp.message_handler(content_types=['web_app_data'])
async def process_web_app_data(message: types.Message):
	"""get web app data"""
	chooser_pers = message.web_app_data.data

	await set_character(message.chat.id, chooser_pers)

	amplitude_log(message.chat.id, "character choosing")

	# getting settings data (started message)
	settings = await get_settings()

	# sending second 'hello' message and removing choose markup
	await message.answer(
		settings.started_message_2,
		reply_markup=types.ReplyKeyboardRemove()
	)
