import os

from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.environ.get("DB_NAME")
USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
HOST = os.environ.get("HOST")
PORT = os.environ.get("PORT")


TELEGRAM_BOT_TOKEN =  os.environ.get("TELEGRAM_BOT_TOKEN")