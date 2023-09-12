from dotenv import load_dotenv

import os

env = load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_HOST = os.getenv("DB_HOST")
DB_PASSWORD = os.getenv("DB_PASSWORD")

AMPLITUDE_API_KEY = os.getenv("AMPLITUDE_KEY")

WEB_PAGE_URL = "https://c63a-45-82-69-182.ngrok-free.app/"

