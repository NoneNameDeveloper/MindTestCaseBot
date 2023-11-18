from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import BigInteger
from sqlalchemy import Integer
from sqlalchemy import DateTime

from engine.db_api.base import Base


class Users(Base):
    """users registered in the bot"""
    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True, index=True, unique=True)
    username = Column(String)
    name = Column(String)
    surname = Column(String)
    registration_datetime = Column(DateTime, default=datetime.now)
    character = Column(String)


class Settings(Base):
    """settings (started message only)"""
    __tablename__ = "settings"

    setting_id = Column(Integer, autoincrement=True, primary_key=True)
    started_message_1 = Column(String, default="👋 <b>Привет!</b>\n🤖 Выбери персонажа, нажав на кнопку снизу.")
    started_message_2 = Column(String, default="✅ Начинай общение, персонаж успешно выбран!")


class Messages(Base):
    """messages from users to AI"""
    __tablename__ = "dialogs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger)
    content = Column(String)
    date_time = Column(DateTime, default=datetime.now)

