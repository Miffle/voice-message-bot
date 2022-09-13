import os
import time
import telebot
import aiogram
from aiogram import *
bot = telebot.TeleBot("XXXXXXXXXXXXXXXXXXXXXXX")


files = os.listdir(".")
print(files)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    for i in range (5, 71):
        if i == (10 or 20 or 30 or 40 or 50 or 60 or 70):
            time.sleep(8)
        else:
            audio = open(files[i], 'rb')
            bot.send_audio(message.chat.id, audio)
            bot.send_message(message.chat.id, audio.name)




bot.polling(none_stop=True)
