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
    return wat2
