from aiogram import types, Dispatcher
from config import bot
from database import db
from keyboards import inline_buttons


async def anketa_questionnaire(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Films or Cartoons and Anime ?",
        reply_markup=await inline_buttons.anketa_first_answers()
    )


async def cartoon_answers(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Your 12 years ?",
    )

async def anime_answers(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Omaeva Muu Shindeyru Noniii?",
    )

async def films_answers(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Films Good boy ?",
    )

def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(anketa_questionnaire,
                                       lambda call: call.data == "anketa_questionnaire")
    dp.register_callback_query_handler(films_answers,
                                       lambda call: call.data == "films")
    dp.register_callback_query_handler(cartoon_answers,
                                       lambda call: call.data == "cartoons")
    dp.register_callback_query_handler(anime_answers,
                                       lambda call: call.data == "anime")