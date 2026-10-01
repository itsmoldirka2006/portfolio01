import telebot
from telebot import types

token="8895520381:AAEnJaIRrNXQ-CTEx0oW0L_0gZdSQ9RU6qY"

bot=telebot.TeleBot(token)u

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id,"hi")

@bot.message_handler(commands=["button"])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("button")
    markup.add(item1)
    bot.send_message(message.chatid,"что надо",reply_markup=markup)
    
@bot.message_handler(content_types="text")
def message_reply(message):
    if message.text == "lol":
        bot.send_message(message.chat,id,"funny")
        
bot.polling()
