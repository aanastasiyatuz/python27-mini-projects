import telebot
from decouple import config


token = config('TOKEN')

# стикеры
yes_sticker = 'CAACAgQAAxkBAAEIBWBkBYbCd3JtgskEfneZSTbFoKVtYwACuQkAAv4x8VDD70Ls7-O9Oy4E'
no_sticker = 'CAACAgQAAxkBAAEIBVlkBYa62TrzaZIbypmMxvUHEYazSgACagoAAo5c-VHYrKOmm55yBi4E'

# клавиатура под сообщением
keyboard = telebot.types.InlineKeyboardMarkup()
b1 = telebot.types.InlineKeyboardButton('Да', callback_data='yes')
b2 = telebot.types.InlineKeyboardButton('Нет', callback_data='no')
keyboard.add(b1, b2)


bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, выбери кнопку', reply_markup=keyboard)

# func - функция фильтр, в данном случае разрешаются все сообщения
@bot.callback_query_handler(func=lambda x: True)
def reply_to_button(call):
    if call.data == 'yes':
        bot.send_sticker(call.from_user.id, yes_sticker)
    elif call.data == 'no':
        bot.send_sticker(call.from_user.id, no_sticker)


bot.polling()
