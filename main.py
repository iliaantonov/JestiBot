from config import *
import telebot
from telebot import types
import random as rand

bot = telebot.TeleBot(token)

i = 0
random = 0

print(execution_urls)
print(execution_descriptions)


# Клавиатура


def keyboard():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_info = types.KeyboardButton('/info')
    button_pain = types.KeyboardButton('/pain')
    button_top = types.KeyboardButton('/top')
    kb.add(button_info)
    kb.add(button_pain)
    kb.add(button_top)
    return kb


# Команды

@bot.message_handler(commands=['start'])
def send_message(message):
    bot.send_message(message.chat.id, '''Здравстуй! Я Жесть-Бот и это последнее сообщение, где я добрый..
\nДля начала лучше прочитай /info
Либо сразу получай видос /pain''', reply_markup=keyboard())


@bot.message_handler(commands=['pain'])
def send_message(message):
    try:
        video_number = rand.randint(0, len(execution_descriptions)-1)

        bot.send_message(message.chat.id, execution_descriptions[video_number],
                         reply_markup=keyboard())
        bot.send_video(message.chat.id, execution_urls[video_number],
                       reply_markup=keyboard())
    except:
        print('URL: ', execution_urls[video_number])
        print('Description: ', execution_descriptions[video_number])
        bot.send_message(message.chat.id, 'Какая-то ошибочка, попробуй ещё раз', reply_markup=keyboard())


@bot.message_handler(commands=['info'])
def send_message(message):
    bot.send_message(message.chat.id, info, reply_markup=keyboard())


# Маты


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Пошёл нахуй' or message.text == 'Пошел нахуй' or message.text == 'пошел нахуй':
        bot.send_message(message.chat.id, 'Мамке своей такое пизди, а я просто бот, хули доебался?')
    if message.text == 'Сука' or message.text == 'сука':
        bot.send_message(message.chat.id, 'Оригинально))0)0)')
    if message.text == 'Бля' or message.text == 'Блять' or message.text == 'бля' or message.text == 'блять':
        bot.send_message(message.chat.id, 'Словарный запас not stonks')
    if message.text == 'Блядь' or message.text == 'блядь':
        bot.send_message(message.chat.id, 'Меня не особо интересует твоё положение в обществе')
    if message.text == 'Бл' or message.text == 'бл':
        bot.send_message(message.chat.id, 'Букву проебал')
    if message.text == 'Пизда' or message.text == 'пизда':
        bot.send_message(message.chat.id, 'Нет')
    if message.text == 'Да' or message.text == 'да':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAOWX8AP6tXmelfkZ1BKdE5FhRNcYTYAAhIBAAJcJ1giCDZ6erYEm1geBA')


@bot.message_handler(content_types=['sticker'])
def send_text(message):
    bot.send_sticker(message.chat.id, stickers_list[rand.randint(1, 38)])


bot.polling()
