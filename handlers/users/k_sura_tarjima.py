from aiogram import types
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from keyboards.default.menu1 import  k_menu1
from keyboards.inline.suralar_tarjimasi import *
from loader import dp, bot

@dp.message_handler(text="Қуръон таржимаси🕋")
async def bot_echo(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer(text='💫',reply_markup=ReplyKeyboardRemove())
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/4',caption=f'<b>Қуръон таржимаси </b> бўлимига ҳуш келибсиз, ўзингизга керакли бўлимни танланг👇',reply_markup=ksuralar)
@dp.message_handler(commands="quron_tarjimasi")
async def bot_echo(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer(text='💫',reply_markup=ReplyKeyboardRemove())
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/4',caption=f'<b>Қуръон таржимаси </b> бўлимига ҳуш келибсиз, ўзингизга керакли бўлимни танланг👇',reply_markup=ksuralar)

@dp.callback_query_handler(text='олдинга')
async def bot_echo(message: CallbackQuery):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/4',caption=f'<b>Қуръон таржимаси </b> бўлимига ҳуш келибсиз, ўзингизга керакли бўлимни танланг👇',
                         reply_markup=ksuralar2)

@dp.callback_query_handler(text='орқага1')
async def bot_echo(message: CallbackQuery):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/4',caption=f'<b>Қуръон таржимаси </b> бўлимига ҳуш келибсиз, ўзингизга керакли бўлимни танланг👇',
                         reply_markup=ksuralar)

@dp.callback_query_handler(text='олдинга1')
async def bot_echo(message: CallbackQuery):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/4',caption=f'<b>Қуръон таржимаси </b> бўлимига ҳуш келибсиз, ўзингизга керакли бўлимни танланг👇',
                         reply_markup=ksuralar3)

@dp.callback_query_handler(text='орқага2')
async def bot_echo(message: CallbackQuery):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/4',caption=f'<b>Қуръон таржимаси </b> бўлимига ҳуш келибсиз, ўзингизга керакли бўлимни танланг👇',
                         reply_markup=ksuralar2)

@dp.callback_query_handler(text='олдинга2')
async def bot_echo(message: CallbackQuery):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/4',caption=f'<b>Қуръон таржимаси </b> бўлимига ҳуш келибсиз, ўзингизга керакли бўлимни танланг👇',
                         reply_markup=ksuralar4)

@dp.callback_query_handler(text='орқага3')
async def bot_echo(message: CallbackQuery):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/4',caption=f'<b>Қуръон таржимаси </b> бўлимига ҳуш келибсиз, ўзингизга керакли бўлимни танланг👇',
                         reply_markup=ksuralar3)

@dp.callback_query_handler(text='олдинга3')
async def bot_echo(message: CallbackQuery):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/4',caption=f'<b>Қуръон таржимаси </b> бўлимига ҳуш келибсиз, ўзингизга керакли бўлимни танланг👇',
                         reply_markup=ksuralar5)

@dp.callback_query_handler(text='орқага4')
async def bot_echo(message: CallbackQuery):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/4',caption=f'<b>Қуръон таржимаси </b> бўлимига ҳуш келибсиз, ўзингизга керакли бўлимни танланг👇',
                         reply_markup=ksuralar4)

@dp.callback_query_handler(text='олдинга4')
async def bot_echo(message: CallbackQuery):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/4',caption=f'<b>Қуръон таржимаси </b> бўлимига ҳуш келибсиз, ўзингизга керакли бўлимни танланг👇',
                         reply_markup=ksuralar6)

@dp.callback_query_handler(text='орқага5')
async def bot_echo(message: CallbackQuery):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/4',caption=f'<b>Қуръон таржимаси </b> бўлимига ҳуш келибсиз, ўзингизга керакли бўлимни танланг👇',
                         reply_markup=ksuralar5)

@dp.callback_query_handler(text='олдинга5')
async def bot_echo(message: CallbackQuery):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/4',caption=f'<b>Қуръон таржимаси </b> бўлимига ҳуш келибсиз, ўзингизга керакли бўлимни танланг👇',
                         reply_markup=ksuralar7)

@dp.callback_query_handler(text='орқага6')
async def bot_echo(message: CallbackQuery):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Namozbot_news/4',caption=f'<b>Қуръон таржимаси </b> бўлимига ҳуш келибсиз, ўзингизга керакли бўлимни танланг👇',
                         reply_markup=ksuralar6)

@dp.callback_query_handler(text='khome')
async def bot_echo(message: CallbackQuery):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await message.message.answer(text=f'O\'zingizga kerakli bo\'limni tanlang👇', reply_markup=k_menu1)










