from aiogram import types

from loader import dp
from keyboards.inline.menu import inline_menu

@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(f'Botni eng yaqin insoningizga ulashing👇',
                         reply_markup=inline_menu)
