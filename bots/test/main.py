import telebot
from decouple import config

token = config('TOKEN')

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello')
    bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAEIBRBkBXYKKioawFvd95EvbKa3wVDFnAACbhcAAqbxcR4JwM32Gb0p8S4E')
    bot.send_photo(message.chat.id, 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_960_720.jpg')

@bot.message_handler(content_types=['text'])
def aaaa(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет')
    else:
        bot.send_message(message.chat.id, 'Сообщение не распознанно')

@bot.message_handler(content_types=['sticker'])
def bbbb(message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)
    bot.send_message(message.chat.id, message.sticker.file_id)


bot.polling()
