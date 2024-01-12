from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


async def anketa_start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Registration",
        callback_data="start_questionnaire"
    )
    markup.add(questionnaire_button)
    return markup

async def anketa_first_answers():
    markup = InlineKeyboardMarkup()
    films_button = InlineKeyboardButton(
        "Films 🎞",
        callback_data="films"
    )
    cartoons_button = InlineKeyboardButton(
        "Cartoons🎑",
        callback_data="cartoons"
    )
    anime_button = InlineKeyboardButton(
        "Anime ⛩",
        callback_data="anime"
    )
    markup.add(films_button)
    markup.add(cartoons_button)
    markup.add(anime_button)
    return markup