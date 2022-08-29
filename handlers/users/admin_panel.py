from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery,ReplyKeyboardRemove

from keyboards.default.menu1 import menu1
from keyboards.inline.til import til
from loader import dp, bot, db
from filters.admin import admin
from keyboards.default.admin_panel import *
from states.holatlar import Forma


@dp.message_handler(admin(), commands='start')
async def bot_echo(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer(text=f"<b>Assalomu alekum boy ota, botingizga hush kelibsiz🙂\n\nMen sizning xizmatingziga shayman🤖</b>", reply_markup=menu_admin)
@dp.callback_query_handler(text='admin_panel')
async def bot_echo(message: CallbackQuery):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await message.message.answer(text=f"Sizning xizmatingziga shayman🤖",reply_markup=menu_admin)

@dp.message_handler(admin(), text="Bot bo'limlari🤖")
async def bot_echo(message: types.Message):
    ism = message.from_user.first_name
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer(text=f'Assalomu aleykum <b>{ism}</b> \n<b>Namoz ilmi</b> botiga xush kelibsiz☺\n'
                              f'Ushbu bot yordamida islomga oid barcha ma\'lumotlarni olishingiz mumkin. '
                              f'\n\n<b>Manba: islom.uz</b>',reply_markup=til)
    await message.answer(text='👨‍💻', reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Bosh Menu🤖', callback_data='admin_panel')
        ]]
    ))

    await message.answer(text=f'O\'zingizga kerakli bo\'limni tanlang👇',)
@dp.message_handler(admin(), text='Admin panel👨‍💻')
async def bot_echo(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer(text='👨‍💻', reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Bosh Menu🤖', callback_data='admin_panel')
        ]]
    ))
    await message.answer(text=f'O\'zingizga kerakli bo\'limni tanlang👇', reply_markup=admin_menu)



""" -----------Admin panel ----------------------"""
@dp.message_handler(admin(), text="Post jo'natish📬")
async def bot_echo(message: types.Message):
    await message.answer(text=f'📬',reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Bosh Menu🤖', callback_data='admin_panel')
        ]]
    ))
    await message.answer(text=f'O\'zingizga kerakli bo\'limni tanlang👇', reply_markup=repost)
@dp.message_handler(admin(), text=f'Statistika📊')
async def bot_echo(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    azo = db.barcha_foydalanuvchilar()
    azolar = azo[-1][0]
    await message.answer(text='📊',reply_markup=ReplyKeyboardRemove())
    await message.answer(text=f'Botdagi a\'zolar soni: {azolar}',reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Bosh Menu🤖', callback_data='admin_panel')
        ]]
    ))

""" ----------- post text ----------------"""
@dp.message_handler(admin(), text='Post text')
async def bot_start(message: types.Message):
    await message.answer('Text xoldagi post yozamiz')
    await message.answer('✍️',reply_markup=ReplyKeyboardRemove())
    await Forma.post_text.set()
@dp.message_handler(admin(), state=Forma.post_text)
async def bot_echo(message: types.Message,state: FSMContext):
    post = message.text
    await state.update_data({'post': post})
    admin = message.from_user.id
    await bot.send_message(chat_id=admin,text=post,reply_markup=post_text)
    await Forma.post_text_jonatish.set()

@dp.message_handler(admin(), state=Forma.post_text_jonatish)
async def bot_echo(message: types.Message, state: FSMContext):
    text = message.text
    admin = message.from_user.id
    data = await state.get_data()
    post = data.get('post')
    if text == 'Text✅':
        users = db.barcha_foydalanuvchilar()
        for user in users:
          await bot.send_message(chat_id=user[4], text=post)
          await bot.send_message(chat_id=admin, text=user)
        await message.answer(text=f'📬', reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text='Bosh Menu🤖', callback_data='admin_panel')
            ]]
        ))
        await bot.send_message(chat_id=admin,text='Text post yuborildi✅',reply_markup=repost)
        await state.finish()
    else:
        await message.answer(text=f'📬', reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text='Bosh Menu🤖', callback_data='admin_panel')
            ]]
        ))
        await bot.send_message(chat_id=admin, text='Text post bekor qilindi❌',reply_markup=repost)
        await state.finish()
""" ----------- post photo ----------------"""

@dp.message_handler(admin(), text='Post photo')
async def bot_echo(message: types.Message,):
    await message.answer('Post uchun rasm jo\'nating🖼',reply_markup=ReplyKeyboardRemove())
    await Forma.post_photo.set()
@dp.message_handler(state=Forma.post_photo, content_types=ContentType.PHOTO)
async def bot_echo(message: types.Message, state: FSMContext):
    photo = message.photo[-1].file_id
    await state.update_data({'photo': photo})
    await message.answer(text='Photo uchun caption jonating')
    await Forma.caption_photo.set()
@dp.message_handler(state=Forma.caption_photo)
async def bot_echo(message: types.Message, state: FSMContext):
    caption = message.text
    admin = message.from_user.id
    await state.update_data({'caption': caption})
    data = await state.get_data()
    photo = data.get('photo')
    caption = data.get('caption')
    await bot.send_photo(chat_id=admin, photo=photo,caption=caption, reply_markup=post_photo)
    await Forma.post_photo_jonatish.set()
@dp.message_handler(state=Forma.post_photo_jonatish)
async def bot_echo(message: types.Message, state: FSMContext):
    data = await state.get_data()
    admin = message.from_user.id
    photo = data.get('photo')
    caption = data.get('caption')
    if message.text == "Photo✅":
        users = db.barcha_foydalanuvchilar()
        for user in users:
            await bot.send_photo(chat_id=user[4], photo=photo,caption=caption)
            await bot.send_message(chat_id=admin, text=user)
        await bot.send_message(chat_id=admin, text='Photo post yuborildi✅', reply_markup=repost)
        await message.answer(text=f'📬', reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(text='Bosh Menu🤖', callback_data='admin_panel')
                ]]
            ))
        await state.finish()
    else:
            await message.answer(text=f'📬', reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(text='Bosh Menu🤖', callback_data='admin_panel')
                ]]
            ))
            await bot.send_message(chat_id=admin, text='Photo post bekor qilindi❌', reply_markup=repost)
            await state.finish()

""" ----------- post video ----------------"""

@dp.message_handler(admin(), text='Post video')
async def bot_echo(message: types.Message,):
    await message.answer('Post uchun video jo\'nating🎥',reply_markup=ReplyKeyboardRemove())
    await Forma.post_video.set()
@dp.message_handler(state=Forma.post_video, content_types=ContentType.VIDEO)
async def bot_echo(message: types.Message, state: FSMContext):
    video = message.video.file_id
    await state.update_data({'video': video})
    await message.answer(text='Video uchun caption jonating')
    await Forma.caption_video.set()
@dp.message_handler(state=Forma.caption_video)
async def bot_echo(message: types.Message, state: FSMContext):
    caption = message.text
    admin = message.from_user.id
    await state.update_data({'caption': caption})
    data = await state.get_data()
    video = data.get('video')
    caption = data.get('caption')
    await bot.send_video(chat_id=admin, video=video,caption=caption, reply_markup=post_video)
    await Forma.post_video_jonatish.set()
@dp.message_handler(state=Forma.post_video_jonatish)
async def bot_echo(message: types.Message, state: FSMContext):
    data = await state.get_data()
    admin = message.from_user.id
    video = data.get('video')
    caption = data.get('caption')
    if message.text == 'Video✅':
        users = db.barcha_foydalanuvchilar()
        for user in users:
            await bot.send_video(chat_id=user[4],video=video,caption=caption)
            await bot.send_message(chat_id=admin, text=user)
        await bot.send_message(chat_id=admin, text='Video post yuborildi✅', reply_markup=repost)
        await message.answer(text=f'📬', reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(text='Bosh Menu🤖', callback_data='admin_panel')
                ]]
            ))
        await state.finish()
    else:
            await message.answer(text=f'📬', reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(text='Bosh Menu🤖', callback_data='admin_panel')
                ]]
            ))
            await bot.send_message(chat_id=admin, text='Photo post bekor qilindi❌', reply_markup=repost)
            await state.finish()