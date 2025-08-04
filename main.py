import telebot

BOT_TOKEN = '8188251065:AAF8TOEa4jSwBTsjFabrL4yt0MTowC8MV3Q'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    greetings = ['Мой Хозяин', 'Господин', 'Отец', 'Царь', 'Мясник']
    from random import choice
    bot.send_message(message.chat.id, f"Приветствую тебя, {choice(greetings)}! Включаю режим МЯСО 🍖")

bot.polling()
