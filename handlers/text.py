from aiogram import types

from engine.service import get_user, add_message
from engine.utils import amplitude_log, fetch_completion
from loader import dp


@dp.message_handler(chat_type='private')
async def get_user_messaage(message: types.Message):
	"""get user message"""
	amplitude_log(message.chat.id, "made a request to AI")

	# getting user from db
	user = await get_user(message.chat.id)

	# getting response from AI
	res = await fetch_completion(message.text, user.character)

	# adding to database
	await add_message(message)

	await message.answer(res)
