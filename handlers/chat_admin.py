import datetime
import sqlite3

from aiogram import types, Dispatcher
from config import bot, GROUP_ID
from database import db
from const import BAN_USER_TEXT
from keyboards import inline_buttons
from profanity_check import predict, predict_prob


async def chat_messages(message: types.Message):
    datab = db.Database()
    print(message.chat.id)
    if message.chat.id == int(GROUP_ID):
        ban_words_predict_prob = predict_prob([message.text])
        print(message.chat)
        if ban_words_predict_prob > 0.8:
            potential = datab.sql_select_ban_user(
                tg_id=message.from_user.id
            )
            print(potential)
            if potential:

                datab.sql_update_ban_count(
                    tg_id=message.from_user.id
                )
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=BAN_USER_TEXT.format(
                        name=message.from_user.first_name,
                        count=potential['count'] + 1
                    )
                )
                if potential['count'] >= 5:

                    await bot.kick_chat_member(message.chat.id,
                                           message.from_user.id)
            elif not potential:
                datab.sql_insert_ban_user(
                    tg_id=message.from_user.id
                )
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=BAN_USER_TEXT.format(
                        name=message.from_user.first_name,
                        count=1
                    )
                )
            await message.delete()


async def check_myself(message: types.Message):
    datab = db.Database()
    potential = datab.sql_select_ban_user(
        tg_id=message.from_user.id
    )
    if potential:
        count = potential['count']
        await message.answer(f'You wrote bad words {count}\n'
                             f'Be careful, you may be kiked')

    else:
        await message.answer('No you didnt write bad words ')
def register_chat_actions_handlers(dp: Dispatcher):
    dp.register_message_handler(check_myself, commands=['check_list'])
    dp.register_message_handler(chat_messages)