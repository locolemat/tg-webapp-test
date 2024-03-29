from telebot.async_telebot import AsyncTelebot
from yaml import load

import os
import asyncio

with open(os.path.join(os.path.dirname(), '..', '..', 'config.yaml')) as f:
    config = load(f)
    TOKEN = config['BOT_TOKEN']

bot = AsyncTelebot("TOKEN")

@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.send_message(chat_id=message.chat.id, text="Hi! I will be hosting a webapp soon!")


asyncio.run(bot.polling())