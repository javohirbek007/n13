import requests
from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline.menu import k_inline_menu
from loader import dp
@dp.callback_query_handler(text='Гулистон')
async def bot_echo(message: CallbackQuery):

  url = "https://aladhan.p.rapidapi.com/timingsByCity"

  querystring = {"country":"Uzbekistan","city":"Toshkent"}

  headers = {
	  "X-RapidAPI-Host": "aladhan.p.rapidapi.com",
	  "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
  }

  responsee = requests.request("GET", url, headers=headers, params=querystring,)

  link = "https://islomapi.uz/api/present/day?region=guliston"

  response = requests.request('GET',link)
  print(response.text)

  kun = responsee.json()['data']['date']['readable']
  hijri_vaqt = responsee.json()['data']['date']['hijri']['date']
  hijr_oyn = responsee.json()['data']['date']['hijri']['month']['number']
  hijr_oy = responsee.json()['data']['date']['hijri']['month']['en']

  hafta_kuni_hijri = responsee.json()['data']['date']['hijri']['weekday']['en']

  kun = response.json()['date']
  hafta_kuni = response.json()['weekday']

  bomdod = response.json()['times']['tong_saharlik']
  quyosh_chiqishi = response.json()['times']['quyosh']
  peshin = response.json()['times']['peshin']
  asr = response.json()['times']['asr']
  shom = response.json()['times']['shom_iftor']
  xufton = response.json()['times']['hufton']
  region = response.json()['region']

  user_id = message.from_user.id
  await message.message.answer(text=f"🔻 Намоз вақтлари: <b>{region}</b>"
                            f"\n\nҚуёш - <b>{quyosh_chiqishi}</b>"
                            f"\nТонг - <b>{bomdod}</b>"
                            f"\nПешин вақти - <b>{peshin}</b>"
                            f"\nАср вақти - <b>{asr}</b>"
                            f"\nШом вақти - <b>{shom}</b>"
                            f"\nХуфтон вақти - <b>{xufton}</b>"
                            f"\n\n<b>{kun} | {hijri_vaqt}</b>",reply_markup=k_inline_menu
                            )
@dp.callback_query_handler(text='Қарши')
async def bot_echo(message: CallbackQuery):

  url = "https://aladhan.p.rapidapi.com/timingsByCity"
  querystring = {"country":"Uzbekistan","city":"Toshkent"}

  headers = {
	  "X-RapidAPI-Host": "aladhan.p.rapidapi.com",
	  "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
  }

  responsee = requests.request("GET", url, headers=headers, params=querystring,)

  link = "https://islomapi.uz/api/present/day?region=qarshi"

  response = requests.request('GET',link)
  print(response.text)

  kun = responsee.json()['data']['date']['readable']
  hijri_vaqt = responsee.json()['data']['date']['hijri']['date']
  hijr_oyn = responsee.json()['data']['date']['hijri']['month']['number']
  hijr_oy = responsee.json()['data']['date']['hijri']['month']['en']

  hafta_kuni_hijri = responsee.json()['data']['date']['hijri']['weekday']['en']

  kun = response.json()['date']
  hafta_kuni = response.json()['weekday']

  bomdod = response.json()['times']['tong_saharlik']
  quyosh_chiqishi = response.json()['times']['quyosh']
  peshin = response.json()['times']['peshin']
  asr = response.json()['times']['asr']
  shom = response.json()['times']['shom_iftor']
  xufton = response.json()['times']['hufton']
  region = response.json()['region']

  user_id = message.from_user.id
  await message.message.answer(text=f"🔻 Намоз вақтлари: <b>{region}</b>"
                            f"\n\nҚуёш - <b>{quyosh_chiqishi}</b>"
                            f"\nТонг - <b>{bomdod}</b>"
                            f"\nПешин вақти - <b>{peshin}</b>"
                            f"\nАср вақти - <b>{asr}</b>"
                            f"\nШом вақти - <b>{shom}</b>"
                            f"\nХуфтон вақти - <b>{xufton}</b>"
                            f"\n\n<b>{kun} | {hijri_vaqt}</b>",reply_markup=k_inline_menu
                            )
@dp.callback_query_handler(text='Урганч')
async def bot_echo(message: CallbackQuery):


  url = "https://aladhan.p.rapidapi.com/timingsByCity"




  querystring = {"country":"Uzbekistan","city":"Toshkent"}

  headers = {
	  "X-RapidAPI-Host": "aladhan.p.rapidapi.com",
	  "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
  }

  responsee = requests.request("GET", url, headers=headers, params=querystring,)

  link = "https://islomapi.uz/api/present/day?region=urganch"

  response = requests.request('GET',link)
  print(response.text)

  kun = responsee.json()['data']['date']['readable']
  hijri_vaqt = responsee.json()['data']['date']['hijri']['date']
  hijr_oyn = responsee.json()['data']['date']['hijri']['month']['number']
  hijr_oy = responsee.json()['data']['date']['hijri']['month']['en']

  hafta_kuni_hijri = responsee.json()['data']['date']['hijri']['weekday']['en']

  kun = response.json()['date']
  hafta_kuni = response.json()['weekday']

  bomdod = response.json()['times']['tong_saharlik']
  quyosh_chiqishi = response.json()['times']['quyosh']
  peshin = response.json()['times']['peshin']
  asr = response.json()['times']['asr']
  shom = response.json()['times']['shom_iftor']
  xufton = response.json()['times']['hufton']
  region = response.json()['region']

  user_id = message.from_user.id
  await message.message.answer(text=f"🔻 Намоз вақтлари: <b>{region}</b>"
                            f"\n\nҚуёш - <b>{quyosh_chiqishi}</b>"
                            f"\nТонг - <b>{bomdod}</b>"
                            f"\nПешин вақти - <b>{peshin}</b>"
                            f"\nАср вақти - <b>{asr}</b>"
                            f"\nШом вақти - <b>{shom}</b>"
                            f"\nХуфтон вақти - <b>{xufton}</b>"
                            f"\n\n<b>{kun} | {hijri_vaqt}</b>",reply_markup=k_inline_menu
                            )
@dp.callback_query_handler(text='Термиз')
async def bot_echo(message: CallbackQuery):


  url = "https://aladhan.p.rapidapi.com/timingsByCity"




  querystring = {"country":"Uzbekistan","city":"Toshkent"}

  headers = {
	  "X-RapidAPI-Host": "aladhan.p.rapidapi.com",
	  "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
  }

  responsee = requests.request("GET", url, headers=headers, params=querystring,)

  link = "https://islomapi.uz/api/present/day?region=termiz"

  response = requests.request('GET',link)
  print(response.text)

  kun = responsee.json()['data']['date']['readable']
  hijri_vaqt = responsee.json()['data']['date']['hijri']['date']
  hijr_oyn = responsee.json()['data']['date']['hijri']['month']['number']
  hijr_oy = responsee.json()['data']['date']['hijri']['month']['en']

  hafta_kuni_hijri = responsee.json()['data']['date']['hijri']['weekday']['en']

  kun = response.json()['date']
  hafta_kuni = response.json()['weekday']

  bomdod = response.json()['times']['tong_saharlik']
  quyosh_chiqishi = response.json()['times']['quyosh']
  peshin = response.json()['times']['peshin']
  asr = response.json()['times']['asr']
  shom = response.json()['times']['shom_iftor']
  xufton = response.json()['times']['hufton']
  region = response.json()['region']

  user_id = message.from_user.id
  await message.message.answer(text=f"🔻 Намоз вақтлари: <b>{region}</b>"
                            f"\n\nҚуёш - <b>{quyosh_chiqishi}</b>"
                            f"\nТонг - <b>{bomdod}</b>"
                            f"\nПешин вақти - <b>{peshin}</b>"
                            f"\nАср вақти - <b>{asr}</b>"
                            f"\nШом вақти - <b>{shom}</b>"
                            f"\nХуфтон вақти - <b>{xufton}</b>"
                            f"\n\n<b>{kun} | {hijri_vaqt}</b>",reply_markup=k_inline_menu
                            )
@dp.callback_query_handler(text='Нукус')
async def bot_echo(message: CallbackQuery):


  url = "https://aladhan.p.rapidapi.com/timingsByCity"




  querystring = {"country":"Uzbekistan","city":"Toshkent"}

  headers = {
	  "X-RapidAPI-Host": "aladhan.p.rapidapi.com",
	  "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
  }

  responsee = requests.request("GET", url, headers=headers, params=querystring,)

  link = "https://islomapi.uz/api/present/day?region=nukus"

  response = requests.request('GET',link)
  print(response.text)

  kun = responsee.json()['data']['date']['readable']
  hijri_vaqt = responsee.json()['data']['date']['hijri']['date']
  hijr_oyn = responsee.json()['data']['date']['hijri']['month']['number']
  hijr_oy = responsee.json()['data']['date']['hijri']['month']['en']

  hafta_kuni_hijri = responsee.json()['data']['date']['hijri']['weekday']['en']

  kun = response.json()['date']
  hafta_kuni = response.json()['weekday']

  bomdod = response.json()['times']['tong_saharlik']
  quyosh_chiqishi = response.json()['times']['quyosh']
  peshin = response.json()['times']['peshin']
  asr = response.json()['times']['asr']
  shom = response.json()['times']['shom_iftor']
  xufton = response.json()['times']['hufton']
  region = response.json()['region']

  user_id = message.from_user.id
  await message.message.answer(text=f"🔻 Намоз вақтлари: <b>{region}</b>"
                            f"\n\nҚуёш - <b>{quyosh_chiqishi}</b>"
                            f"\nТонг - <b>{bomdod}</b>"
                            f"\nПешин вақти - <b>{peshin}</b>"
                            f"\nАср вақти - <b>{asr}</b>"
                            f"\nШом вақти - <b>{shom}</b>"
                            f"\nХуфтон вақти - <b>{xufton}</b>"
                            f"\n\n<b>{kun} | {hijri_vaqt}</b>",reply_markup=k_inline_menu
                            )
@dp.callback_query_handler(text='Хива')
async def bot_echo(message: CallbackQuery):


  url = "https://aladhan.p.rapidapi.com/timingsByCity"




  querystring = {"country":"Uzbekistan","city":"Toshkent"}

  headers = {
	  "X-RapidAPI-Host": "aladhan.p.rapidapi.com",
	  "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
  }

  responsee = requests.request("GET", url, headers=headers, params=querystring,)

  link = "https://islomapi.uz/api/present/day?region=xiva"

  response = requests.request('GET',link)
  print(response.text)

  kun = responsee.json()['data']['date']['readable']
  hijri_vaqt = responsee.json()['data']['date']['hijri']['date']
  hijr_oyn = responsee.json()['data']['date']['hijri']['month']['number']
  hijr_oy = responsee.json()['data']['date']['hijri']['month']['en']

  hafta_kuni_hijri = responsee.json()['data']['date']['hijri']['weekday']['en']

  kun = response.json()['date']
  hafta_kuni = response.json()['weekday']

  bomdod = response.json()['times']['tong_saharlik']
  quyosh_chiqishi = response.json()['times']['quyosh']
  peshin = response.json()['times']['peshin']
  asr = response.json()['times']['asr']
  shom = response.json()['times']['shom_iftor']
  xufton = response.json()['times']['hufton']
  region = response.json()['region']

  user_id = message.from_user.id
  await message.message.answer(text=f"🔻 Намоз вақтлари: <b>{region}</b>"
                            f"\n\nҚуёш - <b>{quyosh_chiqishi}</b>"
                            f"\nТонг - <b>{bomdod}</b>"
                            f"\nПешин вақти - <b>{peshin}</b>"
                            f"\nАср вақти - <b>{asr}</b>"
                            f"\nШом вақти - <b>{shom}</b>"
                            f"\nХуфтон вақти - <b>{xufton}</b>"
                            f"\n\n<b>{kun} | {hijri_vaqt}</b>",reply_markup=k_inline_menu
                            )
@dp.callback_query_handler(text='Андижон')
async def bot_echo(message: CallbackQuery):


  url = "https://aladhan.p.rapidapi.com/timingsByCity"




  querystring = {"country":"Uzbekistan","city":"Toshkent"}

  headers = {
	  "X-RapidAPI-Host": "aladhan.p.rapidapi.com",
	  "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
  }

  responsee = requests.request("GET", url, headers=headers, params=querystring,)

  link = "https://islomapi.uz/api/present/day?region=Andijon"

  response = requests.request('GET',link)
  print(response.text)

  kun = responsee.json()['data']['date']['readable']
  hijri_vaqt = responsee.json()['data']['date']['hijri']['date']
  hijr_oyn = responsee.json()['data']['date']['hijri']['month']['number']
  hijr_oy = responsee.json()['data']['date']['hijri']['month']['en']

  hafta_kuni_hijri = responsee.json()['data']['date']['hijri']['weekday']['en']

  kun = response.json()['date']
  hafta_kuni = response.json()['weekday']

  bomdod = response.json()['times']['tong_saharlik']
  quyosh_chiqishi = response.json()['times']['quyosh']
  peshin = response.json()['times']['peshin']
  asr = response.json()['times']['asr']
  shom = response.json()['times']['shom_iftor']
  xufton = response.json()['times']['hufton']
  region = response.json()['region']

  user_id = message.from_user.id
  await message.message.answer(text=f"🔻 Намоз вақтлари: <b>{region}</b>"
                            f"\n\nҚуёш - <b>{quyosh_chiqishi}</b>"
                            f"\nТонг - <b>{bomdod}</b>"
                            f"\nПешин вақти - <b>{peshin}</b>"
                            f"\nАср вақти - <b>{asr}</b>"
                            f"\nШом вақти - <b>{shom}</b>"
                            f"\nХуфтон вақти - <b>{xufton}</b>"
                            f"\n\n<b>{kun} | {hijri_vaqt}</b>",reply_markup=k_inline_menu
                            )
@dp.callback_query_handler(text='Бухоро')
async def bot_echo(message: CallbackQuery):


  url = "https://aladhan.p.rapidapi.com/timingsByCity"




  querystring = {"country":"Uzbekistan","city":"Toshkent"}

  headers = {
	  "X-RapidAPI-Host": "aladhan.p.rapidapi.com",
	  "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
  }

  responsee = requests.request("GET", url, headers=headers, params=querystring,)

  link = "https://islomapi.uz/api/present/day?region=Buxoro"

  response = requests.request('GET',link)
  print(response.text)

  kun = responsee.json()['data']['date']['readable']
  hijri_vaqt = responsee.json()['data']['date']['hijri']['date']
  hijr_oyn = responsee.json()['data']['date']['hijri']['month']['number']
  hijr_oy = responsee.json()['data']['date']['hijri']['month']['en']

  hafta_kuni_hijri = responsee.json()['data']['date']['hijri']['weekday']['en']

  kun = response.json()['date']
  hafta_kuni = response.json()['weekday']

  bomdod = response.json()['times']['tong_saharlik']
  quyosh_chiqishi = response.json()['times']['quyosh']
  peshin = response.json()['times']['peshin']
  asr = response.json()['times']['asr']
  shom = response.json()['times']['shom_iftor']
  xufton = response.json()['times']['hufton']
  region = response.json()['region']

  user_id = message.from_user.id
  await message.message.answer(text=f"🔻 Намоз вақтлари: <b>{region}</b>"
                            f"\n\nҚуёш - <b>{quyosh_chiqishi}</b>"
                            f"\nТонг - <b>{bomdod}</b>"
                            f"\nПешин вақти - <b>{peshin}</b>"
                            f"\nАср вақти - <b>{asr}</b>"
                            f"\nШом вақти - <b>{shom}</b>"
                            f"\nХуфтон вақти - <b>{xufton}</b>"
                            f"\n\n<b>{kun} | {hijri_vaqt}</b>",reply_markup=k_inline_menu
                            )
@dp.callback_query_handler(text="Фарғона")
async def bot_echo(message: CallbackQuery):


  url = "https://aladhan.p.rapidapi.com/timingsByCity"




  querystring = {"country":"Uzbekistan","city":"Fergana"}

  headers = {
	  "X-RapidAPI-Host": "aladhan.p.rapidapi.com",
	  "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
  }

  responsee = requests.request("GET", url, headers=headers, params=querystring,)

  link = "https://islomapi.uz/api/present/day?region=Farg'оna"

  response = requests.request('GET',link)
  print(response.text)

  kun = responsee.json()['data']['date']['readable']
  hijri_vaqt = responsee.json()['data']['date']['hijri']['date']
  hijr_oyn = responsee.json()['data']['date']['hijri']['month']['number']
  hijr_oy = responsee.json()['data']['date']['hijri']['month']['en']

  hafta_kuni_hijri = responsee.json()['data']['date']['hijri']['weekday']['en']

  kun = response.json()['date']
  hafta_kuni = response.json()['weekday']

  bomdod = response.json()['times']['tong_saharlik']
  quyosh_chiqishi = response.json()['times']['quyosh']
  peshin = response.json()['times']['peshin']
  asr = response.json()['times']['asr']
  shom = response.json()['times']['shom_iftor']
  xufton = response.json()['times']['hufton']
  region = response.json()['region']

  user_id = message.from_user.id
  await message.message.answer(text=f"🔻 Намоз вақтлари: <b>{region}</b>"
                            f"\n\nҚуёш - <b>{quyosh_chiqishi}</b>"
                            f"\nТонг - <b>{bomdod}</b>"
                            f"\nПешин вақти - <b>{peshin}</b>"
                            f"\nАср вақти - <b>{asr}</b>"
                            f"\nШом вақти - <b>{shom}</b>"
                            f"\nХуфтон вақти - <b>{xufton}</b>"
                            f"\n\n<b>{kun} | {hijri_vaqt}</b>",reply_markup=k_inline_menu
                            )
@dp.callback_query_handler(text='Жиззах')
async def bot_echo(message: CallbackQuery):
  url = "https://aladhan.p.rapidapi.com/timingsByCity"
  querystring = {"country":"Uzbekistan","city":"Toshkent"}
  headers = {
	  "X-RapidAPI-Host": "aladhan.p.rapidapi.com",
	  "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
  }
  responsee = requests.request("GET", url, headers=headers, params=querystring,)
  link = "https://islomapi.uz/api/present/day?region=Jizzax"
  response = requests.request('GET',link)
  print(response.text)
  kun = responsee.json()['data']['date']['readable']
  hijri_vaqt = responsee.json()['data']['date']['hijri']['date']
  hijr_oyn = responsee.json()['data']['date']['hijri']['month']['number']
  hijr_oy = responsee.json()['data']['date']['hijri']['month']['en']
  hafta_kuni_hijri = responsee.json()['data']['date']['hijri']['weekday']['en']
  kun = response.json()['date']
  hafta_kuni = response.json()['weekday']
  bomdod = response.json()['times']['tong_saharlik']
  quyosh_chiqishi = response.json()['times']['quyosh']
  peshin = response.json()['times']['peshin']
  asr = response.json()['times']['asr']
  shom = response.json()['times']['shom_iftor']
  xufton = response.json()['times']['hufton']
  region = response.json()['region']
  user_id = message.from_user.id
  await message.message.answer(text=f"🔻 Намоз вақтлари: <b>{region}</b>"
                            f"\n\nҚуёш - <b>{quyosh_chiqishi}</b>"
                            f"\nТонг - <b>{bomdod}</b>"
                            f"\nПешин вақти - <b>{peshin}</b>"
                            f"\nАср вақти - <b>{asr}</b>"
                            f"\nШом вақти - <b>{shom}</b>"
                            f"\nХуфтон вақти - <b>{xufton}</b>"
                            f"\n\n<b>{kun} | {hijri_vaqt}</b>",reply_markup=k_inline_menu
                            )
@dp.callback_query_handler(text='Наманган')
async def bot_echo(message: CallbackQuery):


  url = "https://aladhan.p.rapidapi.com/timingsByCity"




  querystring = {"country":"Uzbekistan","city":"Toshkent"}

  headers = {
	  "X-RapidAPI-Host": "aladhan.p.rapidapi.com",
	  "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
  }

  responsee = requests.request("GET", url, headers=headers, params=querystring,)

  link = "https://islomapi.uz/api/present/day?region=Namangan"

  response = requests.request('GET',link)
  print(response.text)

  kun = responsee.json()['data']['date']['readable']
  hijri_vaqt = responsee.json()['data']['date']['hijri']['date']
  hijr_oyn = responsee.json()['data']['date']['hijri']['month']['number']
  hijr_oy = responsee.json()['data']['date']['hijri']['month']['en']

  hafta_kuni_hijri = responsee.json()['data']['date']['hijri']['weekday']['en']

  kun = response.json()['date']
  hafta_kuni = response.json()['weekday']

  bomdod = response.json()['times']['tong_saharlik']
  quyosh_chiqishi = response.json()['times']['quyosh']
  peshin = response.json()['times']['peshin']
  asr = response.json()['times']['asr']
  shom = response.json()['times']['shom_iftor']
  xufton = response.json()['times']['hufton']
  region = response.json()['region']

  user_id = message.from_user.id
  await message.message.answer(text=f"🔻 Намоз вақтлари: <b>{region}</b>"
                            f"\n\nҚуёш - <b>{quyosh_chiqishi}</b>"
                            f"\nТонг - <b>{bomdod}</b>"
                            f"\nПешин вақти - <b>{peshin}</b>"
                            f"\nАср вақти - <b>{asr}</b>"
                            f"\nШом вақти - <b>{shom}</b>"
                            f"\nХуфтон вақти - <b>{xufton}</b>"
                            f"\n\n<b>{kun} | {hijri_vaqt}</b>",reply_markup=k_inline_menu
                            )
@dp.callback_query_handler(text='Navoiy')
async def bot_echo(message: CallbackQuery):


  url = "https://aladhan.p.rapidapi.com/timingsByCity"




  querystring = {"country":"Uzbekistan","city":"Toshkent"}

  headers = {
	  "X-RapidAPI-Host": "aladhan.p.rapidapi.com",
	  "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
  }

  responsee = requests.request("GET", url, headers=headers, params=querystring,)

  link = "https://islomapi.uz/api/present/day?region=Navoiy"

  response = requests.request('GET',link)
  print(response.text)

  kun = responsee.json()['data']['date']['readable']
  hijri_vaqt = responsee.json()['data']['date']['hijri']['date']
  hijr_oyn = responsee.json()['data']['date']['hijri']['month']['number']
  hijr_oy = responsee.json()['data']['date']['hijri']['month']['en']

  hafta_kuni_hijri = responsee.json()['data']['date']['hijri']['weekday']['en']

  kun = response.json()['date']
  hafta_kuni = response.json()['weekday']

  bomdod = response.json()['times']['tong_saharlik']
  quyosh_chiqishi = response.json()['times']['quyosh']
  peshin = response.json()['times']['peshin']
  asr = response.json()['times']['asr']
  shom = response.json()['times']['shom_iftor']
  xufton = response.json()['times']['hufton']
  region = response.json()['region']

  user_id = message.from_user.id
  await message.message.answer(text=f"🔻 Намоз вақтлари: <b>{region}</b>"
                            f"\n\nҚуёш - <b>{quyosh_chiqishi}</b>"
                            f"\nТонг - <b>{bomdod}</b>"
                            f"\nПешин вақти - <b>{peshin}</b>"
                            f"\nАср вақти - <b>{asr}</b>"
                            f"\nШом вақти - <b>{shom}</b>"
                            f"\nХуфтон вақти - <b>{xufton}</b>"
                            f"\n\n<b>{kun} | {hijri_vaqt}</b>",reply_markup=k-inline_menu
                            )
@dp.callback_query_handler(text='Самарқанд')
async def bot_echo(message: CallbackQuery):


  url = "https://aladhan.p.rapidapi.com/timingsByCity"




  querystring = {"country":"Uzbekistan","city":"Toshkent"}

  headers = {
	  "X-RapidAPI-Host": "aladhan.p.rapidapi.com",
	  "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
  }

  responsee = requests.request("GET", url, headers=headers, params=querystring,)

  link = "https://islomapi.uz/api/present/day?region=Samarqand"

  response = requests.request('GET',link)
  print(response.text)

  kun = responsee.json()['data']['date']['readable']
  hijri_vaqt = responsee.json()['data']['date']['hijri']['date']
  hijr_oyn = responsee.json()['data']['date']['hijri']['month']['number']
  hijr_oy = responsee.json()['data']['date']['hijri']['month']['en']

  hafta_kuni_hijri = responsee.json()['data']['date']['hijri']['weekday']['en']

  kun = response.json()['date']
  hafta_kuni = response.json()['weekday']

  bomdod = response.json()['times']['tong_saharlik']
  quyosh_chiqishi = response.json()['times']['quyosh']
  peshin = response.json()['times']['peshin']
  asr = response.json()['times']['asr']
  shom = response.json()['times']['shom_iftor']
  xufton = response.json()['times']['hufton']
  region = response.json()['region']

  user_id = message.from_user.id
  await message.message.answer(text=f"🔻 Намоз вақтлари: <b>{region}</b>"
                            f"\n\nҚуёш - <b>{quyosh_chiqishi}</b>"
                            f"\nТонг - <b>{bomdod}</b>"
                            f"\nПешин вақти - <b>{peshin}</b>"
                            f"\nАср вақти - <b>{asr}</b>"
                            f"\nШом вақти - <b>{shom}</b>"
                            f"\nХуфтон вақти - <b>{xufton}</b>"
                            f"\n\n<b>{kun} | {hijri_vaqt}</b>",reply_markup=k_inline_menu
                            )
@dp.callback_query_handler(text='Тошкент')
async def bot_echo(message: CallbackQuery):


  url = "https://aladhan.p.rapidapi.com/timingsByCity"




  querystring = {"country":"Uzbekistan","city":"Toshkent"}

  headers = {
	  "X-RapidAPI-Host": "aladhan.p.rapidapi.com",
	  "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
  }

  responsee = requests.request("GET", url, headers=headers, params=querystring,)

  link = "https://islomapi.uz/api/present/day?region=Toshkent"

  response = requests.request('GET',link)
  print(response.text)

  kun = responsee.json()['data']['date']['readable']
  hijri_vaqt = responsee.json()['data']['date']['hijri']['date']
  hijr_oyn = responsee.json()['data']['date']['hijri']['month']['number']
  hijr_oy = responsee.json()['data']['date']['hijri']['month']['en']

  hafta_kuni_hijri = responsee.json()['data']['date']['hijri']['weekday']['en']

  kun = response.json()['date']
  hafta_kuni = response.json()['weekday']

  bomdod = response.json()['times']['tong_saharlik']
  quyosh_chiqishi = response.json()['times']['quyosh']
  peshin = response.json()['times']['peshin']
  asr = response.json()['times']['asr']
  shom = response.json()['times']['shom_iftor']
  xufton = response.json()['times']['hufton']
  region = response.json()['region']

  user_id = message.from_user.id
  await message.message.answer(text=f"🔻 Намоз вақтлари: <b>{region}</b>"
                            f"\n\nҚуёш - <b>{quyosh_chiqishi}</b>"
                            f"\nТонг - <b>{bomdod}</b>"
                            f"\nПешин вақти - <b>{peshin}</b>"
                            f"\nАср вақти - <b>{asr}</b>"
                            f"\nШом вақти - <b>{shom}</b>"
                            f"\nХуфтон вақти - <b>{xufton}</b>"
                            f"\n\n<b>{kun} | {hijri_vaqt}</b>",reply_markup=k_inline_menu
                            )
@dp.callback_query_handler(text='намоз')
async def bot_echo(message: CallbackQuery):
  bomdod = f'<b>Bomdod namozi</b>\n'\
           f'Субҳи содиқдан (чин тонг отгандан) кун чиққунчадир.' \
           f'Бомдод намозини тонг ёришганда ўқиш мустаҳаб,' \
           f'аълороқдир. Соат бўйича ҳисобланса, бомдодни кун чиқишидан 40 дақиқача илгари ўқиш мустаҳаб вақтига мувофиқ бўлади.'
  peshin = f'<b>Пешин намози</b>\n' \
           f'Қуёш заволга (оғишга) кетганидан сўнг то нарсаларнинг сояси қуёш тиккага келган пайтдаги соясидан ташқари ўз узунлигига нисбатан икки баравар ортгунига қадар. ' \
           f'Пешин намозини ёз фаслида бироз кечиктириб, қиш фаслида эса вақти кириши билан ўқиш мустаҳабдир.'
  asr = f'<b>Аср намози</b>\n' \
        f'Ҳар бир нарсанинг сояси қуёш тиккага келган пайтдаги соясидан ташқари ўзига нисбатан икки баравар ортганидан бошлаб қуёш ботгунчадир.' \
        f'Аср намозини қуёш тиғини ўзгартирмай, нурсиз ҳолатга киришидан олдинроқ ўқиш мустаҳабдир.'
  shom = f'<b>Шом намози</b>\n' \
           f'Кун ботган пайтдан бошлаб кунботар томонда шафақ (қизғиш нурлар) ғойиб бўлгунчадир.' \
           f'Шом намозини доимо қуёш ботиши билан ўқиш мустаҳабдир.'
  xufton = f'<b>Хуфтон намози</b>\n' \
             f'Шафақ батамом йўқолгандан кейин киради.' \
             f'Хуфтон намозини кечанинг учдан бирининг охирида ўқиш афзал ва ниҳоятда аъло бўлади.'
  vitr = f'<b>Витр намози</b>\n' \
           f'Хуфтон ўқилгандан кейингина киради. Хуфтон ва витр намозларини субҳи содиққача ўқиса бўлади.' \
           f'Витр намозини тун охирида уйғонишга қодир бўлган кишилар субҳ олдидан ўқисалар, мустаҳаб амал қилган бўлишади.'
  await message.message.answer(text=f'{bomdod}\n\n'
                                    f'{peshin}\n\n'
                                    f'{asr}\n\n'
                                    f'{shom}\n\n'
                                    f'{xufton}\n\n'
                                    f'{vitr}', reply_markup=k_inline_menu
                               )

