from telebot.async_telebot import AsyncTeleBot
from telebot.util import quick_markup
from telebot.types import WebAppData, WebAppInfo
from yaml import safe_load

import os
import asyncio

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', 'config.yaml')) as f:
    config = safe_load(f)
    TOKEN = config['BOT_TOKEN']

bot = AsyncTeleBot(TOKEN)

@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    markup = quick_markup({
        "Open a webapp":{'web_app': WebAppInfo('http://localhost:3500')}
    }, row_width=1)
    await bot.send_message(chat_id=message.chat.id, text="Hi! I will be hosting a webapp soon!", reply_markup=markup)
    


asyncio.run(bot.polling())