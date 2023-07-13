#! /usr/bin/python3

import telebot
from telebot import types
import os
from add_image_text import add_text

token_file = open('token.txt', 'r')
token_id = token_file.read()
bot = telebot.TeleBot(token_id)

@bot.message_handler(commands=['start', 'help'])
def start(message):
    mess = f'Hi, {message.from_user.first_name}!\nI am FunnyTextBot, I can add your text to a picture, send me one and follow the instructions. Have fun :)'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(content_types=['photo'])
def photo(message):
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("img/"+str(message.chat.id)+".jpg", 'wb') as mess_photo:
        mess_photo.write(downloaded_file)
    bot.send_message(message.chat.id, 'Photo received, let\'s add text!', parse_mode='html')

@bot.message_handler(content_types=['text'])
def answer(message):
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    # start = types.KeyboardButton("/start")
    # help = types.KeyboardButton("/help")
    # markup.add(start, help)        
    if (os.path.exists("img/"+str(message.chat.id)+".jpg")):
        add_text("img/"+str(message.chat.id), message.text)
        ans_photo = open("img/"+str(message.chat.id)+"ans.jpg", 'rb')
        bot.send_photo(message.chat.id, ans_photo)
        os.remove("img/"+str(message.chat.id)+".jpg")
        os.remove("img/"+str(message.chat.id)+"ans.jpg")
    else:
        bot.send_message(message.chat.id, 'Send me a picture', parse_mode='html')

bot.polling(non_stop=True)