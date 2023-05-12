import telebot
from googletrans import Translator
from langdetect import detect

translator = Translator()

bot = telebot.TeleBot('')


@bot.message_handler(func=lambda m: True)
def translate_massage(message):
    src = detect(message.text)
    dest = 'ru'
    translated_text = translator.translate(message.text, src=src, dest=dest).text
    bot.send_message(message.chat.id, translated_text)


bot.polling(none_stop=True)
