from tg_bot import Tg_Bot
import telebot
from config import API_TOKEN, token

scraping = Tg_Bot()
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    scraping.last_two(message)

@bot.message_handler(commands=['sql'])
def sql(message):
    scraping.sql1(message)


bot.infinity_polling()
