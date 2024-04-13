from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
import app.keyboards as kb
import database as db

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет! В этом боте вы можете посмотреть успеваемость своего ребенка. В это меню можно '
                         'вернуться в любой момент, написав в чат /start. Нажмите начать', reply_markup=kb.main)


@router.callback_query(lambda callback_query: any(callback_query.data == clb for clb in ['start', 'back']))
async def start(callback: CallbackQuery):
    await callback.message.edit_text('Выберите имя:', reply_markup=await kb.inline_names())


@router.callback_query(lambda callback_query: callback_query.data.startswith('name_'))
async def show_marks(query: CallbackQuery):
    i = int(query.data.split('_')[1])
    await query.message.edit_text(f'{db.names[i]}, оценки:\nАнглийский язык🇬🇧\n {str(db.marks[0][i])[1:-1]} | '
                                  f'{round(sum(db.marks[0][i]) / len(db.marks[0][i]), 2)}\n'
                                  f'Биология🌱\n {str(db.marks[1][i])[1:-1]} | '
                                  f'{round(sum(db.marks[1][i]) / len(db.marks[1][i]), 2)}\n'
                                  f'География🌍\n {str(db.marks[2][i])[1:-1]} | '
                                  f'{round(sum(db.marks[2][i]) / len(db.marks[2][i]), 2)}\n'
                                  f'Информатика💻\n {str(db.marks[3][i])[1:-1]} | '
                                  f'{round(sum(db.marks[3][i]) / len(db.marks[3][i]), 2)}\n'
                                  f'История🏛️\n {str(db.marks[4][i])[1:-1]} | '
                                  f'{round(sum(db.marks[4][i]) / len(db.marks[4][i]), 2)}\n'
                                  f'Литература📚\n {str(db.marks[5][i])[1:-1]} | '
                                  f'{round(sum(db.marks[5][i]) / len(db.marks[5][i]), 2)}\n'
                                  f'Математика📏\n {str(db.marks[6][i])[1:-1]} | '
                                  f'{round(sum(db.marks[6][i]) / len(db.marks[6][i]), 2)}\n'
                                  f'Русский язык📝\n {str(db.marks[7][i])[1:-1]} | '
                                  f'{round(sum(db.marks[7][i]) / len(db.marks[7][i]), 2)}\n'
                                  f'Физика🌌\n {str(db.marks[8][i])[1:-1]} | '
                                  f'{round(sum(db.marks[8][i]) / len(db.marks[8][i]), 2)}\n'
                                  f'Физкультура🏊‍♂️\n {str(db.marks[9][i])[1:-1]} | '
                                  f'{round(sum(db.marks[9][i]) / len(db.marks[9][i]), 2)}\n'
                                  f'Химия⚗️\n {str(db.marks[10][i])[1:-1]} | '
                                  f'{round(sum(db.marks[10][i]) / len(db.marks[10][i]), 2)}\n'
                                  f'Обществознание📊\n {str(db.marks[11][i])[1:-1]} | '
                                  f'{round(sum(db.marks[11][i]) / len(db.marks[11][i]), 2)}\n', reply_markup=kb.go_back)


