from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.default.menu1 import menu1, k_menu1
from keyboards.inline.til import til
from loader import dp, db,bot


@dp.message_handler(commands='start')
async def bot_start(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    ism = message.from_user.first_name
    familya = message.from_user.last_name
    username = message.from_user.username
    tg_id = message.from_user.id
    try:
        db.user_qoshish(ism=ism, familya=familya, username=username, tg_id=tg_id)

    except Exception as xatolik:
        print(xatolik)
    await message.answer(f'Yozuv turini tanlang! / Ёзув турини танланг!',reply_markup=til)


@dp.callback_query_handler(text='lotin')
async def til_lotin(message: CallbackQuery):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    ism = message.from_user.first_name
    await message.message.answer(
        text=f'Assalomu aleykum <b>{ism}</b> \n<b>Namoz ilmi</b> botiga xush kelibsiz☺\n'
             f'Ushbu bot yordamida islomga oid barcha ma\'lumotlarni olishingiz mumkin. '
             f'\n\n<b>Manba: islom.uz</b>')
    await message.message.answer(
        text=f'O\'zingizga kerakli bo\'limni tanlang👇', reply_markup=menu1)

@dp.callback_query_handler(text='krill')
async def til_lotin(message: CallbackQuery):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    ism = message.from_user.first_name
    await message.message.answer(
        text=f'Ассалому алейкум <b>{ism}</b>\n<b>Намоз илми</b> ботига хуш келибсиз☺ '
             f'\nУшбу бот ёрдамида исломга оид барча маълумотларни олишингиз мумкин. \n\n'
             f'<b>Манба: islom.uz</b>')
    await message.message.answer(
        text=f'Ўзингизга керакли бўлимни танланг👇', reply_markup=k_menu1)

