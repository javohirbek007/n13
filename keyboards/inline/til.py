from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

til = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Lotin🇺🇿',callback_data='lotin'),
            InlineKeyboardButton(text='Крилл🇺🇿',callback_data='krill')
        ],
    ]
)