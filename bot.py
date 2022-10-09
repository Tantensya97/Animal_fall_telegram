import telebot
from telebot import types 
TOKEN = '5776921296:AAHUM13GK22QSWaBV3fXQBefb8LpGJgr3U4'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    item1 = types.KeyboardButton('Скачать игру')

    markup.add(item1)

    bot.send_message(message.chat.id, 'Здравствуй, {0.first_name}!'.format(message.from_user), reply_markup= markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Скачать игру':
            bot.send_message(message.chat.id, 'https://clck.ru/32Hx7E')

bot.polling(none_stop= True)