from main import bot, dp
from aiogram.types import Message
from config import admin_id
from database import PushUserSmsInDb, ShowUserMessage


async def send_to_admin(*args):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")


# @dp.message_handler(content_types=['photo', 'text', 'video', 'audio', 'sticker'])
# async def printing(message):
#     print ( )
#     print ( )
#     print(message)
#     PushUserSmsInDb(message)
#     ShowUserMessage(message.from_user.id)
#     await message.reply(text=message)


@dp.message_handler()
async def echo(message: Message):
    text = f"привет писака: {message.text} \n"
    wat = f"письмо отправлено: {message.date} \n"
    wat2 = f"ваш id: {message.from_user.id} \n"
    wat3 = f"ваше имя: {message.from_user.first_name} \n"
    wat4 = f"ваша фамилия: {message.from_user.last_name} \n"
    wat5 = f"ваш ник: {message.from_user.username} \n"
    wat6 = f"id сообщения: {message.message_id} \n"
    message_text = message.text
    file_id = 'none'
    file_type = 'text'
    PushUserSmsInDb ( message, file_id , file_type , message_text)
    await message.reply(text=text + wat + wat2 + wat3 + wat4 + wat5 + wat6)

@dp.message_handler(content_types=['photo', 'text'])
async def handle_docs_photo(message):
    photo_id = message.photo[-1].file_id

    print ( )
    print ( )
    print(message.photo[-1].file_id)
    file_id = message.photo[-1].file_id
    file_type = 'photo'
    message_text = message.caption
    PushUserSmsInDb ( message ,file_id, file_type,message_text)

@dp.message_handler(content_types=['video'])
async def video_file_id(message):
    print ( )
    print ( )
    print(message.video.thumb.file_id)
    file_id = message.video.thumb.file_id
    file_type = 'video'
    message_text = message.caption
    PushUserSmsInDb ( message, file_id, file_type,message_text)

@dp.message_handler(content_types=['audio'])
async def audio_file_id(message):
    print ( )
    print ( )
    print(message.audio.file_id)
    file_id = message.audio.file_id
    file_type = 'audio'
    message_text = message.caption
    PushUserSmsInDb ( message, file_id, file_type,message_text)

@dp.message_handler(content_types=['sticker'])
async def sticker_file_id(message):
    print()
    print ( )
    print(message.sticker.thumb.file_id)
    file_id=message.sticker.thumb.file_id
    file_type = 'sticker'
    message_text = message.caption
    PushUserSmsInDb ( message, file_id, file_type,message_text)