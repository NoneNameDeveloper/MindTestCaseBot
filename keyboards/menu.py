from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo


class Reply:

	@staticmethod
	def web_app_markup(uri: str):
		"""character choosing web app"""
		web_app = WebAppInfo(url=uri)

		markup = ReplyKeyboardMarkup(resize_keyboard=True)

		btn1 = KeyboardButton("Выбор персонажа", web_app=web_app)

		markup.add(btn1)

		return markup
