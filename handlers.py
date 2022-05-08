from main import bot, dp
from aiogram.types import Message
from config import admin_id
import database

async def send_to_admin(*args):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")


@dp.message_handler()
async def echo(message: Message):
    text = f"привет писака: {message.text} \n"
    wat = f"письмо отправлено: {message.date} \n"
    wat2 = f"ваш id: {message.from_user.id} \n"
    wat3 = f"ваше имя: {message.from_user.first_name} \n"
    wat4 = f"ваша фамилия: {message.from_user.last_name} \n"
    wat5 = f"ваш ник: {message.from_user.username} \n"
    wat6 = f"id сообщения: {message.message_id} \n"

    print(message)
    await message.reply(text=text + wat + wat2+ wat3+ wat4+ wat5+ wat6)


@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message):
    photo_id = message.photo[-1].file_id
    await bot.send_photo(message.from_user.id, photo_id)
    await bot.send_photo(-454011048, photo_id)