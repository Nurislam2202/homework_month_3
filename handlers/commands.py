from aiogram import types, Dispatcher
from config import bot
import os
from aiogram.types import InputFile
import random


async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Привет!')
    await message.answer(text='Привет')


async def info_handler(message: types.Message):
    await message.answer('Nurislam test bot from the first homework')


async def mem_handler(message: types.Message):
    path = 'media/'
    files = []

    for f in os.listdir(path):
        full_path = os.path.join(path, f)
        if os.path.isfile(full_path):
            files.append(full_path)

    random_photo = random.choice(files)
    await message.answer_photo(photo=InputFile(random_photo))


async def files_handler(message: types.Message):
    path = 'files/'
    files = []

    for f in os.listdir(path):
        full_path = os.path.join(path, f)
        if os.path.isfile(full_path):
            files.append(full_path)

    random_file = random.choice(files)
    await message.answer_document(document=InputFile(random_file))


def register_commands(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(info_handler, commands=['info'])
    dp.register_message_handler(mem_handler, commands=['mem', 'photo'])
    dp.register_message_handler(mem_handler, text='отправь мем')
    dp.register_message_handler(files_handler, text='отправь файл')
