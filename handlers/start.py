import sqlite3

from aiogram import types, Dispatcher
from config import bot
from database import db
from keyboards import inline_buttons

async def anketa_start_button(message: types.Message):
    datab = db.Database()
    datab.sql_insert_user(
        tg_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )
    print(message)
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f"Hello Hi {message.from_user.first_name}",
        reply_markup=await inline_buttons.anketa_start_keyboard()
    )


def register_anketa_start_handlers(dp: Dispatcher):
    dp.register_message_handler(anketa_start_button, commands=['go', 'start'])

