from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def register() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Start registration', callback_data='register')]
    ])

    return kb


def language() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('English', callback_data='EN'),
         InlineKeyboardButton('Russian', callback_data='RU'),
         InlineKeyboardButton('Indonesian', callback_data='IN')]
    ])

    return kb