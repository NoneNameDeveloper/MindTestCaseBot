import json

import aiohttp
from aiogram import types

from amplitude import Identify, BaseEvent
from sqlalchemy import insert, select

from config import WEB_PAGE_URL
from engine.db_api import Users, Settings
from engine.db_api.base import get_session
from engine.service import get_user, create_user
from keyboards.menu import Reply
from loader import amplitude


def amplitude_log(
        user_id: int | None = None,
        event: str | None = None
):
    identify_obj = Identify()
    amplitude.identify(identify_obj, event_options={"option": "test case"})

    amplitude.track(
        BaseEvent(
            event_type=event,
            user_id=str(user_id),
        )
    )

    # flush the event buffer
    amplitude.flush()


async def get_started_message_1() -> str:
    """get started message from settings db"""
    session = await get_session()

    stmt = select(Settings)
    res = await session.execute(stmt)

    await session.close()

    return res.scalar().started_message_1


async def process_start(message: types.Message):
    """handling start message"""

    started_message: str = await get_started_message_1()

    user = await get_user(message.chat.id)

    # new user (not in database)
    if not user:
        amplitude_log(message.chat.id, "Registered")

        await create_user(message)

        return await message.answer(started_message, reply_markup=Reply.web_app_markup(WEB_PAGE_URL))

    # user haven`t got character chosen
    if not user.character:
        return await message.answer(started_message, reply_markup=Reply.web_app_markup(WEB_PAGE_URL))

    # user writing /start again
    else:
        return await message.answer(started_message)


async def process_menu(message):
    """handling menu command"""
    return await message.answer("👱‍♂️ Перейдите к выбору персонажа по кнопке ниже.", reply_markup=Reply.web_app_markup(WEB_PAGE_URL))


async def fetch_completion(prompt: str, character: str):
    """getting data from gpt3.5"""
    if character == "mario":
        extra = "You are Mario from Super Mario.\n"
    else:
        extra = "You are scientist Albert Einshtein.\n"

    messages = [
            {"role": "user", "content": extra + prompt}
        ]

    endpoint = 'http://95.217.14.178:8080/candidates_openai/gpt'

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    data = {
        'model': 'gpt-3.5-turbo',
        'messages': messages,
    }

    data = json.dumps(data)

    async with aiohttp.ClientSession() as session:
        async with session.post(endpoint, headers=headers, data=data) as response:

            resp = await response.json()
            return resp['choices'][0]['message']['content']
