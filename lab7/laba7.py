import telebot
import os
from dotenv import load_dotenv

# Завантажуємо токен з .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

# Обробка текстових повідомлень
@bot.message_handler(content_types=['text'])
def echo_text(message):
    bot.send_message(message.chat.id, message.text)

# Обробка фото (з підписом або без)
@bot.message_handler(content_types=['photo'])
def echo_photo(message):
    file_id = message.photo[-1].file_id  # беремо фото найкращої якості
    caption = message.caption if message.caption else None
    bot.send_photo(message.chat.id, file_id, caption=caption)

# Обробка голосових
@bot.message_handler(content_types=['voice'])
def echo_voice(message):
    bot.send_voice(message.chat.id, message.voice.file_id)

# Обробка документів
@bot.message_handler(content_types=['document'])
def echo_document(message):
    bot.send_document(message.chat.id, message.document.file_id)

# Обробка відео
@bot.message_handler(content_types=['video'])
def echo_video(message):
    bot.send_video(message.chat.id, message.video.file_id)

# Обробка стікерів
@bot.message_handler(content_types=['sticker'])
def echo_sticker(message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)

# Обробка аудіо
@bot.message_handler(content_types=['audio'])
def echo_audio(message):
    bot.send_audio(message.chat.id, message.audio.file_id)

# Обробка всього іншого
@bot.message_handler(content_types=['animation', 'video_note', 'contact', 'location'])
def echo_other(message):
    bot.forward_message(message.chat.id, message.chat.id, message.message_id)

bot.polling(none_stop=True)
