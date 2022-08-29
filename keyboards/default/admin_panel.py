from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_admin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Bot bo'limlari🤖"),
            KeyboardButton(text='Admin panel👨‍💻'),
        ],
    ],
    resize_keyboard=True
)
admin_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Post jo'natish📬"),
            KeyboardButton(text='Statistika📊'),
        ],
    ],
    resize_keyboard=True
)
repost = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Post text'),
            KeyboardButton(text='Post photo'),
        ],
        [
            KeyboardButton(text='Post video')
        ]

    ],
    resize_keyboard=True
)

post_text = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Text❌"),
            KeyboardButton(text='Text✅'),
        ],
    ],
    resize_keyboard=True
)

post_photo = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Photo❌"),
            KeyboardButton(text='Photo✅'),
        ],
    ],
    resize_keyboard=True
)

post_video = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Video❌"),
            KeyboardButton(text='Video✅'),
        ],
    ],
    resize_keyboard=True
)