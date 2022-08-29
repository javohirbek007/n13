from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu1 = ReplyKeyboardMarkup(
    keyboard=[
         [
            KeyboardButton(text='Namoz vaqtlari🕰'),
        ],

        [
            KeyboardButton(text="Qur'ondan darslar📖"),
        ],
        [
            KeyboardButton(text="Qur'on tarjimasi🕋"),
        ],
[
            KeyboardButton(text='Makkayu Madinaga sayohat🕋'),
        ],

        [
            KeyboardButton(text='Darsliklar📚'),
        ],
[
            KeyboardButton(text='Botni baholash🌟'),
        ],
    ],
    resize_keyboard=True

)

k_menu1 = ReplyKeyboardMarkup(
    keyboard=[
         [
            KeyboardButton(text='Намоз вақтлари🕰'),
        ],

        [
            KeyboardButton(text="Қуръондан дарслар📖"),
        ],
        [
            KeyboardButton(text="Қуръон таржимаси🕋"),
        ],
[
            KeyboardButton(text='Маккаю Мадинага саёҳат🕋'),
        ],

        [
            KeyboardButton(text='Дарсликлар📚'),
        ],
[
            KeyboardButton(text='Ботни баҳолаш🌟'),
        ],
    ],
    resize_keyboard=True

)

vaqtdan_orqaga = ReplyKeyboardMarkup(
    keyboard=[
         [
            KeyboardButton(text='Ortga🔙'),
        ],
    ],
    resize_keyboard=True

)

k_vaqtdan_orqaga = ReplyKeyboardMarkup(
    keyboard=[
         [
            KeyboardButton(text='Ортга🔙'),
        ],
    ],
    resize_keyboard=True

)