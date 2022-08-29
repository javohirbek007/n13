from aiogram import types
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.menu1 import *
from keyboards.inline.kirish import *
from loader import dp,bot
from keyboards.inline.menu import *


@dp.message_handler(text='Намоз вақтлари🕰')
async def bot_echo(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer(text='💫', reply_markup=k_vaqtdan_orqaga)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/2',caption=f'<b>Намоз вақтлари</b> бўлимига ҳуш келибсиз, ўзингизга керакли ҳудудни танланг👇',
                         reply_markup=k_viloyat)

@dp.message_handler(text='Ортга🔙')
async def bot_echo(message: types.Message):
    await message.answer(
        text=f'Ўзингизга керакли бўлимни танланг👇', reply_markup=k_menu1)
@dp.message_handler(text="Қуръондан дарслар📖")
async def bot_echo(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer(text='💫', reply_markup=k_vaqtdan_orqaga)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/3',caption=f'<b>Қуръондан дарслар</b> бўлимига ҳуш келибсиз, ўзингизга керакли бўлимни танланг👇',
                         reply_markup=k_darslar)

@dp.message_handler(text='Дарсликлар📚')
async def bot_echo(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer(text='💫', reply_markup=k_vaqtdan_orqaga)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/6',caption=f'<b>Дарсликлар</b> бўлимига ҳуш келибсиз, ўзингизга керакли бўлимни танланг👇',
                         reply_markup=k_darsliklar)

@dp.message_handler(text='Маккаю Мадинага саёҳат🕋',)
async def bot_echo(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer(text='💫', reply_markup=k_vaqtdan_orqaga)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/5',caption=f'<b>Маккаю Мадинага саёҳат🕋</b> бўлимига ҳуш келибсиз. Бу бўлимда сиз <b>Макка ва Мадинаъ</b>ни онлайн <b>жонли эфир\'</b>да кузатишингиз мумкин, ўзингизга керакли бўлимни танланг👇',
                         reply_markup=k_makka_va_madina)

@dp.message_handler(text='Ботни баҳолаш🌟')
async def bot_echo(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer(f'🌟', reply_markup=ReplyKeyboardRemove())
    await message.answer(f'<b>Намоз</b> ботдан фойдаланганиз учун раҳмат.\n'
                         f'Бот фаолиятини янада яхшилаш учун 5 баллик тизим асосида баҳоланг👇\n\n'
                         f'<b>Жуда зўр -</b> 🌟🌟🌟🌟🌟\n'
                         f'<b>Яхши -</b>     🌟🌟🌟🌟\n'
                         f'<b>Зўр эмас -</b> 🌟🌟🌟\n'
                         f'<b>Ёмон -</b>      🌟🌟\n'
                         f'<b>Жуда ёмон -</b> 🌟',reply_markup=klike)
@dp.callback_query_handler(text='k1')
async def bot_echo(callback: types.CallbackQuery):
    name = callback.from_user.first_name
    user = callback.from_user.username
    id = callback.from_user.id
    await bot.send_message(chat_id=5445755536,text=f'Foydalanuvchi({name}) Id: {id}, username: @{user} botni 1 ball bilan baholadi')
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('Бизга лойиқ деб билган баҳойингиздан мамнунмиз, <b>Баҳолаганингиз учун рахмат😊</b>',reply_markup=k_menu1)
@dp.callback_query_handler(text='k2')
async def bot_echo(callback: types.CallbackQuery):
    name = callback.from_user.first_name
    user = callback.from_user.username
    id = callback.from_user.id
    await bot.send_message(chat_id=5445755536,text=f'Foydalanuvchi({name}) Id: {id}, username: @{user} botni 2 ball bilan baholadi')
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('Бизга лойиқ деб билган баҳойингиздан мамнунмиз, <b>Баҳолаганингиз учун рахмат😊</b>',reply_markup=k_menu1)
@dp.callback_query_handler(text='k3')
async def bot_echo(callback: types.CallbackQuery):
    name = callback.from_user.first_name
    user = callback.from_user.username
    id = callback.from_user.id
    await bot.send_message(chat_id=5445755536,text=f'Foydalanuvchi({name}) Id: {id}, username: @{user} botni 3 ball bilan baholadi')
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('Бизга лойиқ деб билган баҳойингиздан мамнунмиз, <b>Баҳолаганингиз учун рахмат😊</b>',reply_markup=k_menu1)
@dp.callback_query_handler(text='k4')
async def bot_echo(callback: types.CallbackQuery):
    name = callback.from_user.first_name
    user = callback.from_user.username
    id = callback.from_user.id
    await bot.send_message(chat_id=5445755536,text=f'Foydalanuvchi({name}) Id: {id}, username: @{user} botni 4 ball bilan baholadi')
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('Бизга лойиқ деб билган баҳойингиздан мамнунмиз, <b>Баҳолаганингиз учун рахмат😊</b>',reply_markup=k_menu1)
@dp.callback_query_handler(text='k5')
async def bot_echo(callback: types.CallbackQuery):
    name = callback.from_user.first_name
    user = callback.from_user.username
    id = callback.from_user.id
    await bot.send_message(chat_id=5445755536,text=f'Foydalanuvchi({name}) Id: {id}, username: @{user} botni 5 ball bilan baholadi')
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('Бизга лойиқ деб билган баҳойингиздан мамнунмиз, <b>Баҳолаганингиз учун рахмат😊</b>',reply_markup=k_menu1)







