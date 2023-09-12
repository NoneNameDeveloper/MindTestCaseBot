from aiogram import executor, types
from sqlalchemy import select, func, insert

import handlers
from engine.db_api import Settings
from engine.db_api.base import init_models, get_session

from loader import dp, amplitude


async def create_settings():
	"""create settings if not exist"""
	session = await get_session()

	statement = select(func.count()).select_from(Settings)
	count = await session.execute(statement)

	count: int = count.scalar()

	if count == 0:
		stmt = insert(Settings).values()

		await session.execute(stmt)
		await session.commit()
		await session.close()


async def set_default_commands(dp):
	await dp.bot.set_my_commands([
		types.BotCommand("start", "Запустить бота"),
		types.BotCommand("menu", "Смена персонажа")
	])


async def on_startup(dp):
	await init_models()

	await create_settings()

	await set_default_commands(dp)


async def on_shutdown(dp):
	amplitude.shutdown()


if __name__ == "__main__":
	executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
