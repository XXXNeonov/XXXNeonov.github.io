import telebot
from telebot import types

bot = telebot.TeleBot("token")

web_app_url = "t.me/svetacoin_bot/webapp"

text = "Тапаем Свету!\n\nНажми на кнопку снизу, что заработать ни-ху-я!"

button = types.InlineKeyboardButton('Проебать время', url=web_app_url)
keyboard = types.InlineKeyboardMarkup()
keyboard.add(button)

@bot.message_handler(commands=['start'])
def send_message(message):
    bot.send_message(message.chat.id, text=text, reply_markup=keyboard)

bot.polling()
