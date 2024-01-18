from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


async def anketa_start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Questionnaire",
        callback_data="start_questionnaire"
    )
    registration_button = InlineKeyboardButton(
        "Start Registration ",
        callback_data="registration"
    )
    markup.add(questionnaire_button)
    markup.add(registration_button)
    return markup

async def questionnaire_first_answers():
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