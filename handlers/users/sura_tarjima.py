from aiogram import types
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from keyboards.default.menu1 import menu1
from keyboards.inline.suralar_tarjimasi import *
from loader import dp, bot

@dp.message_handler(text="Qur'on tarjimasi🕋")
async def bot_echo(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer(text='💫',reply_markup=ReplyKeyboardRemove())
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/4',caption=f'<b>Qur\'on tarjimasi</b> bo\'limiga hush kelibsiz, o\'zingizga kerakli bo\'limni tanlang👇',reply_markup=suralar)
@dp.message_handler(commands="quron_tarjimasi")
async def bot_echo(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer(text='💫',reply_markup=ReplyKeyboardRemove())
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/4',caption=f'<b>Qur\'on tarjimasi</b> bo\'limiga hush kelibsiz, o\'zingizga kerakli bo\'limni tanlang👇',reply_markup=suralar)

@dp.callback_query_handler(text='oldinga')
async def bot_echo(message: CallbackQuery):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/4',caption=f'<b>Qur\'on tarjimasi</b> bo\'limiga hush kelibsiz, o\'zingizga kerakli bo\'limni tanlang👇',
                         reply_markup=suralar2)

@dp.callback_query_handler(text='orqaga1')
async def bot_echo(message: CallbackQuery):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/4',caption=f'<b>Qur\'on tarjimasi</b> bo\'limiga hush kelibsiz, o\'zingizga kerakli bo\'limni tanlang👇',
                         reply_markup=suralar)

@dp.callback_query_handler(text='oldinga1')
async def bot_echo(message: CallbackQuery):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/4',caption=f'<b>Qur\'on tarjimasi</b> bo\'limiga hush kelibsiz, o\'zingizga kerakli bo\'limni tanlang👇',
                         reply_markup=suralar3)

@dp.callback_query_handler(text='orqaga2')
async def bot_echo(message: CallbackQuery):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/4',caption=f'<b>Qur\'on tarjimasi</b> bo\'limiga hush kelibsiz, o\'zingizga kerakli bo\'limni tanlang👇',
                         reply_markup=suralar2)

@dp.callback_query_handler(text='oldinga2')
async def bot_echo(message: CallbackQuery):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/4',caption=f'<b>Qur\'on tarjimasi</b> bo\'limiga hush kelibsiz, o\'zingizga kerakli bo\'limni tanlang👇',
                         reply_markup=suralar4)

@dp.callback_query_handler(text='orqaga3')
async def bot_echo(message: CallbackQuery):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/4',caption=f'<b>Qur\'on tarjimasi</b> bo\'limiga hush kelibsiz, o\'zingizga kerakli bo\'limni tanlang👇',
                         reply_markup=suralar3)

@dp.callback_query_handler(text='oldinga3')
async def bot_echo(message: CallbackQuery):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/4',caption=f'<b>Qur\'on tarjimasi</b> bo\'limiga hush kelibsiz, o\'zingizga kerakli bo\'limni tanlang👇',
                         reply_markup=suralar5)

@dp.callback_query_handler(text='orqaga4')
async def bot_echo(message: CallbackQuery):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/4',caption=f'<b>Qur\'on tarjimasi</b> bo\'limiga hush kelibsiz, o\'zingizga kerakli bo\'limni tanlang👇',
                         reply_markup=suralar4)

@dp.callback_query_handler(text='oldinga4')
async def bot_echo(message: CallbackQuery):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/4',caption=f'<b>Qur\'on tarjimasi</b> bo\'limiga hush kelibsiz, o\'zingizga kerakli bo\'limni tanlang👇',
                         reply_markup=suralar6)

@dp.callback_query_handler(text='orqaga5')
async def bot_echo(message: CallbackQuery):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/4',caption=f'<b>Qur\'on tarjimasi</b> bo\'limiga hush kelibsiz, o\'zingizga kerakli bo\'limni tanlang👇',
                         reply_markup=suralar5)

@dp.callback_query_handler(text='oldinga5')
async def bot_echo(message: CallbackQuery):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/4',caption=f'<b>Qur\'on tarjimasi</b> bo\'limiga hush kelibsiz, o\'zingizga kerakli bo\'limni tanlang👇',
                         reply_markup=suralar7)

@dp.callback_query_handler(text='orqaga6')
async def bot_echo(message: CallbackQuery):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/4',caption=f'<b>Qur\'on tarjimasi</b> bo\'limiga hush kelibsiz, o\'zingizga kerakli bo\'limni tanlang👇',
                         reply_markup=suralar6)

@dp.callback_query_handler(text='home')
async def bot_echo(message: CallbackQuery):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await message.message.answer(text=f'O\'zingizga kerakli bo\'limni tanlang👇', reply_markup=menu1)










