import telebot, dotenv, os

from telebot import types

import requests
dotenv.load_dotenv()

def gencat():
    url='https://api.thecatapi.com/v1/images/search'
    response=requests.get(url)
    return response.json()[0]['url']
def gendog():
    url='https://dog.ceo/api/breeds/image/random'
    response=requests.get(url)
    return response.json()['message']
token=os.getenv('BOT')
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Сгенерировать котика")
    item2=types.KeyboardButton("Сгенерировать собачку")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id,"Привет, этот бот нужен для генерации котиков и собачек.", reply_markup=markup)
@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Сгенерировать котика":
        bot.send_photo(message.chat.id, gencat())
    if message.text=="Сгенерировать собачку":
        bot.send_photo(message.chat.id, gendog())
bot.polling()