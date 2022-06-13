import os
import sqlite3

import vk_api
import telebot
from config import API_TOKEN, token

bot = telebot.TeleBot(API_TOKEN)
session = vk_api.VkApi(token=token)

class Tg_Bot:

    def last_two(self, message):
        '''
        при команде старт отправляет 2 последних объявления в чат
        :return:
        '''
        domain = 'arenda_v_moskv'
        count = 2
        offset = 0
        wall = session.method('wall.get', {'domain': domain,
                                           'count': count,
                                           'offset': offset})
        all_post = []
        all_post.append(wall)
        for post in all_post[0]['items']:
            print(post['text'])
            print(post['attachments'][-1]['link']['url'])
            bot.send_message(message.chat.id, f"{post['text']} {post['attachments'][-1]['link']['url']}")

    def sql1(self, message):
        bot.send_message(message.chat.id, 'test')
        print('test')

class Scraping_db:

    def __init__(self, Scraping_db):
        self.Scraping_db = Scraping_db

    def connect(self):
        if not os.path.exists(self.Scraping_db):
            print('Error not file')  # можно создать
        self.sqlite = sqlite3.connect(self.Scraping_db)  # создаем таблицу с именем в скобках


