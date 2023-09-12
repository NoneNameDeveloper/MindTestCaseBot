from sqlalchemy import insert, select, update

from engine.db_api import Users, Settings, Messages

from engine.db_api.base import get_session


async def get_user(user_id: int) -> Users:
	"""get user from db"""
	session = await get_session()

	stmt = select(Users).where(Users.user_id == user_id)
	user_ = await session.execute(stmt)
	user = user_.scalar()

	await session.close()

	return user


async def create_user(
		message
):
	"""creating user"""
	session = await get_session()

	stmt = insert(Users).values(
		user_id=message.chat.id,
		username=message.from_user.username,
		name=message.from_user.first_name,
		surname=message.from_user.last_name
	)

	await session.execute(stmt)
	await session.commit()

	await session.close()


async def set_character(user_id: int, character: str):
	"""set character to user"""
	session = await get_session()

	stmt = update(Users).where(Users.user_id == user_id).values(character=character.lower())

	await session.execute(stmt)
	await session.commit()
	await session.close()


async def get_settings() -> Settings:
	"""getting settings data"""
	session = await get_session()

	stmt = select(Settings)

	res_ = await session.execute(stmt)

	await session.close()

	return res_.scalar()


async def add_message(message):
	"""adding message to messages"""
	session = await get_session()

	stmt = insert(Messages).values(
		user_id=message.chat.id,
		content=message.text
	)
	await session.execute(stmt)
	await session.commit()
	await session.close()
