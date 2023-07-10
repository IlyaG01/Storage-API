from telebot import TeleBot, apihelper, util
from telebot.apihelper import ApiTelegramException
from telebot.types import Message

import config 

bot = TeleBot(config.TELEGRAM_BOT_TOKEN)

def send_message_to_employee(user_id: int, user_from_whom:str, text: str):
    text_message = text + "\n\n" + "Отправил: " + user_from_whom
    bot.send_message(user_id, text_message, "")
