from aiogram import types
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.menu1 import vaqtdan_orqaga, menu1
from keyboards.inline.kirish import darslar, darsliklar, makka_va_madina
from loader import dp,bot
from keyboards.inline.menu import viloyat, like



# Echo bot
@dp.message_handler(text='Namoz vaqtlari🕰')
async def bot_echo(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer(text='💫', reply_markup=vaqtdan_orqaga)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/2',caption=f'<b>Namoz vaqtlari</b> bo\'limiga hush kelibsiz, o\'zingizga kerakli hududni tanlang👇',
                         reply_markup=viloyat)
@dp.message_handler(commands='namoz_vaqtlari')
async def bot_echo(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer(text='💫', reply_markup=vaqtdan_orqaga)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/2',caption=f'<b>Namoz vaqtlari</b> bo\'limiga hush kelibsiz, o\'zingizga kerakli hududni tanlang👇',
                         reply_markup=viloyat)
@dp.message_handler(text='Ortga🔙')
async def bot_echo(message: types.Message):
    await message.answer(
        text=f'O\'zingizga kerakli bo\'limni tanlang👇', reply_markup=menu1)
@dp.message_handler(text="Qur'ondan darslar📖")
async def bot_echo(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer(text='💫', reply_markup=vaqtdan_orqaga)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/3',caption=f'<b>Qur\'ondan darslar</b> bo\'limiga hush kelibsiz, o\'zingizga kerakli bo\'limni tanlang👇',
                         reply_markup=darslar)
@dp.message_handler(commands="qurondan_darslar")
async def bot_echo(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer(text='💫', reply_markup=vaqtdan_orqaga)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/3',caption=f'<b>Qur\'ondan darslar</b> bo\'limiga hush kelibsiz, o\'zingizga kerakli bo\'limni tanlang👇',
                         reply_markup=darslar)
@dp.message_handler(text='Darsliklar📚')
async def bot_echo(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer(text='💫', reply_markup=vaqtdan_orqaga)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/6',caption=f'<b>Darsliklar</b> bo\'limiga hush kelibsiz, o\'zingizga kerakli bo\'limni tanlang👇',
                         reply_markup=darsliklar)
@dp.message_handler(commands='darsliklar')
async def bot_echo(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer(text='💫', reply_markup=vaqtdan_orqaga)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/6',caption=f'<b>Darsliklar</b> bo\'limiga hush kelibsiz, o\'zingizga kerakli bo\'limni tanlang👇',
                         reply_markup=darsliklar)
@dp.message_handler(commands='jonli_efir')
async def bot_echo(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer(text='💫', reply_markup=vaqtdan_orqaga)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/5',caption=f'<b>Makkayu Madinaga sayohat🕋</b> bo\'limiga hush kelibsiz. Bu bo\'limda siz <b>Makka va Madina\'</b>ni onlayn <b>jonli efir</b>da kuzatishingiz mumkin, o\'zingizga kerakli bo\'limni tanlang👇',
                         reply_markup=makka_va_madina)
@dp.message_handler(text='Makkayu Madinaga sayohat🕋',)
async def bot_echo(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer(text='💫', reply_markup=vaqtdan_orqaga)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/5',caption=f'<b>Makkayu Madinaga sayohat🕋</b> bo\'limiga hush kelibsiz. Bu bo\'limda siz <b>Makka va Madina\'</b>ni onlayn <b>jonli efir</b>da kuzatishingiz mumkin, o\'zingizga kerakli bo\'limni tanlang👇',
                         reply_markup=makka_va_madina)

@dp.message_handler(text='Botni baholash🌟')
async def bot_echo(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer(f'🌟', reply_markup=ReplyKeyboardRemove())
    await message.answer(f'<b>Namoz</b> botdan foydalanganiz uchun rahmat.\n'
                         f'Bot faoliyatini yanada yaxshilash uchun 5 ballik tizim asosida baholang👇\n\n'
                         f'<b>Juda zo\'r -</b> 🌟🌟🌟🌟🌟\n'
                         f'<b>Yaxshi -</b>     🌟🌟🌟🌟\n'
                         f'<b>Zo\'r emas -</b> 🌟🌟🌟\n'
                         f'<b>Yomon -</b>      🌟🌟\n'
                         f'<b>Juda yomon -</b> 🌟',reply_markup=like)
@dp.callback_query_handler(text='1')
async def bot_echo(callback: types.CallbackQuery):
    name = callback.from_user.first_name
    user = callback.from_user.username
    id = callback.from_user.id
    await bot.send_message(chat_id=5445755536,text=f'Foydalanuvchi({name}) Id: {id}, username: @{user} botni 1 ball bilan baholadi')
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('Bizga loyiq deb bilgan bahoyingizdan mamnunmiz, <b>Baholaganingiz uchun raxmat😊</b>',reply_markup=menu1)
@dp.callback_query_handler(text='2')
async def bot_echo(callback: types.CallbackQuery):
    name = callback.from_user.first_name
    user = callback.from_user.username
    id = callback.from_user.id
    await bot.send_message(chat_id=5445755536,text=f'Foydalanuvchi({name}) Id: {id}, username: @{user} botni 2 ball bilan baholadi')
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('Bizga loyiq deb bilgan bahoyingizdan mamnunmiz, <b>Baholaganingiz uchun raxmat😊</b>',reply_markup=menu1)
@dp.callback_query_handler(text='3')
async def bot_echo(callback: types.CallbackQuery):
    name = callback.from_user.first_name
    user = callback.from_user.username
    id = callback.from_user.id
    await bot.send_message(chat_id=5445755536,text=f'Foydalanuvchi({name}) Id: {id}, username: @{user} botni 3 ball bilan baholadi')
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('Bizga loyiq deb bilgan bahoyingizdan mamnunmiz, <b>Baholaganingiz uchun raxmat😊</b>',reply_markup=menu1)
@dp.callback_query_handler(text='4')
async def bot_echo(callback: types.CallbackQuery):
    name = callback.from_user.first_name
    user = callback.from_user.username
    id = callback.from_user.id
    await bot.send_message(chat_id=5445755536,text=f'Foydalanuvchi({name}) Id: {id}, username: @{user} botni 4 ball bilan baholadi')
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('Bizga loyiq deb bilgan bahoyingizdan mamnunmiz, <b>Baholaganingiz uchun raxmat😊</b>',reply_markup=menu1)
@dp.callback_query_handler(text='5')
async def bot_echo(callback: types.CallbackQuery):
    name = callback.from_user.first_name
    user = callback.from_user.username
    id = callback.from_user.id
    await bot.send_message(chat_id=5445755536,text=f'Foydalanuvchi({name}) Id: {id}, username: @{user} botni 5 ball bilan baholadi')
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('Bizga loyiq deb bilgan bahoyingizdan mamnunmiz, <b>Baholaganingiz uchun raxmat😊</b>',reply_markup=menu1)







