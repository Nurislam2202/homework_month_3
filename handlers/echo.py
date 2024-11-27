from aiogram import types, Dispatcher


async def number_handler(message: types.Message):
    try:
        num = float(message.text)
        squared = num ** 2
        await message.answer(f'квадрат числа {num} равен {squared}')
    except ValueError:
        await message.answer(message.text)


def register_message(dp: Dispatcher):
    dp.register_message_handler(number_handler)
