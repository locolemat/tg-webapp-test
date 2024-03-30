from telebot.async_telebot import AsyncTeleBot
from yaml import safe_load

import os
import asyncio

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', 'config.yaml')) as f:
    config = safe_load(f)
    TOKEN = config['BOT_TOKEN']

bot = AsyncTeleBot(TOKEN)

@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.send_message(chat_id=message.chat.id, text="Hi! I will be hosting a webapp soon!")


asyncio.run(bot.polling())