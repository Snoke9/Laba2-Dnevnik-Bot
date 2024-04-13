from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
import database as db


names = db.names


async def inline_names():
    keyboard = InlineKeyboardBuilder()
    for name in names:
        keyboard.add(InlineKeyboardButton(text=name, callback_data=f'name_{names.index(name)}'))
    return keyboard.adjust(2).as_markup()

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Начать', callback_data='start')]
    ])

go_back = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='⬅Назад', callback_data='back')]])
