import requests
from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline.menu import inline_menu
from loader import dp
@dp.callback_query_handler(text='Guliston')
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
  await message.message.answer(text=f"🔻 Namoz vaqtlari: <b>{region}</b>"
                            f"\n\nQuyosh - <b>{quyosh_chiqishi}</b>"
                            f"\nTong - <b>{bomdod}</b>"
                            f"\nPeshin vaqti - <b>{peshin}</b>"
                            f"\nAsr vaqti - <b>{asr}</b>"
                            f"\nShom vaqti - <b>{shom}</b>"
                            f"\nXufton vaqti - <b>{xufton}</b>"
                            f"\n\n<b>{kun} | {hijri_vaqt}</b>"
                            f"\n<b>{hijr_oy}</b>  oyning, <b>{hafta_kuni_hijri}</b> kuni"
                            f"\nHaftaning <b>{hafta_kuni}</b> kuni",reply_markup=inline_menu
                            )
@dp.callback_query_handler(text='Qarshi')
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
  await message.message.answer(text=f"🔻 Namoz vaqtlari: <b>{region}</b>"
                            f"\n\nQuyosh - <b>{quyosh_chiqishi}</b>"
                            f"\nTong - <b>{bomdod}</b>"
                            f"\nPeshin vaqti - <b>{peshin}</b>"
                            f"\nAsr vaqti - <b>{asr}</b>"
                            f"\nShom vaqti - <b>{shom}</b>"
                            f"\nXufton vaqti - <b>{xufton}</b>"
                            f"\n\n<b>{kun} | {hijri_vaqt}</b>"
                            f"\n<b>{hijr_oy}</b>  oyning, <b>{hafta_kuni_hijri}</b> kuni"
                            f"\nHaftaning <b>{hafta_kuni}</b> kuni",reply_markup=inline_menu
                            )
@dp.callback_query_handler(text='Urganch')
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
  await message.message.answer(text=f"🔻 Namoz vaqtlari: <b>{region}</b>"
                            f"\n\nQuyosh - <b>{quyosh_chiqishi}</b>"
                            f"\nTong - <b>{bomdod}</b>"
                            f"\nPeshin vaqti - <b>{peshin}</b>"
                            f"\nAsr vaqti - <b>{asr}</b>"
                            f"\nShom vaqti - <b>{shom}</b>"
                            f"\nXufton vaqti - <b>{xufton}</b>"
                            f"\n\n<b>{kun} | {hijri_vaqt}</b>"
                            f"\n<b>{hijr_oy}</b>  oyning, <b>{hafta_kuni_hijri}</b> kuni"
                            f"\nHaftaning <b>{hafta_kuni}</b> kuni",reply_markup=inline_menu
                            )
@dp.callback_query_handler(text='Termiz')
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
  await message.message.answer(text=f"🔻 Namoz vaqtlari: <b>{region}</b>"
                            f"\n\nQuyosh - <b>{quyosh_chiqishi}</b>"
                            f"\nTong - <b>{bomdod}</b>"
                            f"\nPeshin vaqti - <b>{peshin}</b>"
                            f"\nAsr vaqti - <b>{asr}</b>"
                            f"\nShom vaqti - <b>{shom}</b>"
                            f"\nXufton vaqti - <b>{xufton}</b>"
                            f"\n\n<b>{kun} | {hijri_vaqt}</b>"
                            f"\n<b>{hijr_oy}</b>  oyning, <b>{hafta_kuni_hijri}</b> kuni"
                            f"\nHaftaning <b>{hafta_kuni}</b> kuni",reply_markup=inline_menu
                            )
@dp.callback_query_handler(text='Nukus')
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
  await message.message.answer(text=f"🔻 Namoz vaqtlari: <b>{region}</b>"
                            f"\n\nQuyosh - <b>{quyosh_chiqishi}</b>"
                            f"\nTong - <b>{bomdod}</b>"
                            f"\nPeshin vaqti - <b>{peshin}</b>"
                            f"\nAsr vaqti - <b>{asr}</b>"
                            f"\nShom vaqti - <b>{shom}</b>"
                            f"\nXufton vaqti - <b>{xufton}</b>"
                            f"\n\n<b>{kun} | {hijri_vaqt}</b>"
                            f"\n<b>{hijr_oy}</b>  oyning, <b>{hafta_kuni_hijri}</b> kuni"
                            f"\nHaftaning <b>{hafta_kuni}</b> kuni",reply_markup=inline_menu
                            )
@dp.callback_query_handler(text='Xiva')
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
  await message.message.answer(text=f"🔻 Namoz vaqtlari: <b>{region}</b>"
                            f"\n\nQuyosh - <b>{quyosh_chiqishi}</b>"
                            f"\nTong - <b>{bomdod}</b>"
                            f"\nPeshin vaqti - <b>{peshin}</b>"
                            f"\nAsr vaqti - <b>{asr}</b>"
                            f"\nShom vaqti - <b>{shom}</b>"
                            f"\nXufton vaqti - <b>{xufton}</b>"
                            f"\n\n<b>{kun} | {hijri_vaqt}</b>"
                            f"\n<b>{hijr_oy}</b>  oyning, <b>{hafta_kuni_hijri}</b> kuni"
                            f"\nHaftaning <b>{hafta_kuni}</b> kuni",reply_markup=inline_menu
                            )
@dp.callback_query_handler(text='Andijon')
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
  await message.message.answer(text=f"🔻 Namoz vaqtlari: <b>{region}</b>"
                            f"\n\nQuyosh - <b>{quyosh_chiqishi}</b>"
                            f"\nTong - <b>{bomdod}</b>"
                            f"\nPeshin vaqti - <b>{peshin}</b>"
                            f"\nAsr vaqti - <b>{asr}</b>"
                            f"\nShom vaqti - <b>{shom}</b>"
                            f"\nXufton vaqti - <b>{xufton}</b>"
                            f"\n\n<b>{kun} | {hijri_vaqt}</b>"
                            f"\n<b>{hijr_oy}</b>  oyning, <b>{hafta_kuni_hijri}</b> kuni"
                            f"\nHaftaning <b>{hafta_kuni}</b> kuni",reply_markup=inline_menu
                            )
@dp.callback_query_handler(text='Buxoro')
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
  await message.message.answer(text=f"🔻 Namoz vaqtlari: <b>{region}</b>"
                            f"\n\nQuyosh - <b>{quyosh_chiqishi}</b>"
                            f"\nTong - <b>{bomdod}</b>"
                            f"\nPeshin vaqti - <b>{peshin}</b>"
                            f"\nAsr vaqti - <b>{asr}</b>"
                            f"\nShom vaqti - <b>{shom}</b>"
                            f"\nXufton vaqti - <b>{xufton}</b>"
                            f"\n\n<b>{kun} | {hijri_vaqt}</b>"
                            f"\n<b>{hijr_oy}</b>  oyning, <b>{hafta_kuni_hijri}</b> kuni"
                            f"\nHaftaning <b>{hafta_kuni}</b> kuni",reply_markup=inline_menu
                            )
@dp.callback_query_handler(text="Farg'ona")
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
  await message.message.answer(text=f"🔻 Namoz vaqtlari: <b>{region}</b>"
                            f"\n\nQuyosh - <b>{quyosh_chiqishi}</b>"
                            f"\nTong - <b>{bomdod}</b>"
                            f"\nPeshin vaqti - <b>{peshin}</b>"
                            f"\nAsr vaqti - <b>{asr}</b>"
                            f"\nShom vaqti - <b>{shom}</b>"
                            f"\nXufton vaqti - <b>{xufton}</b>"
                            f"\n\n<b>{kun} | {hijri_vaqt}</b>"
                            f"\n<b>{hijr_oy}</b>  oyning, <b>{hafta_kuni_hijri}</b> kuni"
                            f"\nHaftaning <b>{hafta_kuni}</b> kuni",reply_markup=inline_menu
                            )
@dp.callback_query_handler(text='Jizzax')
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
  await message.message.answer(text=f"🔻 Namoz vaqtlari: <b>{region}</b>"
                            f"\n\nQuyosh - <b>{quyosh_chiqishi}</b>"
                            f"\nTong - <b>{bomdod}</b>"
                            f"\nPeshin vaqti - <b>{peshin}</b>"
                            f"\nAsr vaqti - <b>{asr}</b>"
                            f"\nShom vaqti - <b>{shom}</b>"
                            f"\nXufton vaqti - <b>{xufton}</b>"
                            f"\n\n<b>{kun} | {hijri_vaqt}</b>"
                            f"\n<b>{hijr_oy}</b>  oyning, <b>{hafta_kuni_hijri}</b> kuni"
                            f"\nHaftaning <b>{hafta_kuni}</b> kuni",reply_markup=inline_menu
                            )
@dp.callback_query_handler(text='Namangan')
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
  await message.message.answer(text=f"🔻 Namoz vaqtlari: <b>{region}</b>"
                            f"\n\nQuyosh - <b>{quyosh_chiqishi}</b>"
                            f"\nTong - <b>{bomdod}</b>"
                            f"\nPeshin vaqti - <b>{peshin}</b>"
                            f"\nAsr vaqti - <b>{asr}</b>"
                            f"\nShom vaqti - <b>{shom}</b>"
                            f"\nXufton vaqti - <b>{xufton}</b>"
                            f"\n\n<b>{kun} | {hijri_vaqt}</b>"
                            f"\n<b>{hijr_oy}</b>  oyning, <b>{hafta_kuni_hijri}</b> kuni"
                            f"\nHaftaning <b>{hafta_kuni}</b> kuni",reply_markup=inline_menu
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
  await message.message.answer(text=f"🔻 Namoz vaqtlari: <b>{region}</b>"
                            f"\n\nQuyosh - <b>{quyosh_chiqishi}</b>"
                            f"\nTong - <b>{bomdod}</b>"
                            f"\nPeshin vaqti - <b>{peshin}</b>"
                            f"\nAsr vaqti - <b>{asr}</b>"
                            f"\nShom vaqti - <b>{shom}</b>"
                            f"\nXufton vaqti - <b>{xufton}</b>"
                            f"\n\n<b>{kun} | {hijri_vaqt}</b>"
                            f"\n<b>{hijr_oy}</b>  oyning, <b>{hafta_kuni_hijri}</b> kuni"
                            f"\nHaftaning <b>{hafta_kuni}</b> kuni",reply_markup=inline_menu
                            )
@dp.callback_query_handler(text='Samarqand')
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
  await message.message.answer(text=f"🔻 Namoz vaqtlari: <b>{region}</b>"
                            f"\n\nQuyosh - <b>{quyosh_chiqishi}</b>"
                            f"\nTong - <b>{bomdod}</b>"
                            f"\nPeshin vaqti - <b>{peshin}</b>"
                            f"\nAsr vaqti - <b>{asr}</b>"
                            f"\nShom vaqti - <b>{shom}</b>"
                            f"\nXufton vaqti - <b>{xufton}</b>"
                            f"\n\n<b>{kun} | {hijri_vaqt}</b>"
                            f"\n<b>{hijr_oy}</b>  oyning, <b>{hafta_kuni_hijri}</b> kuni"
                            f"\nHaftaning <b>{hafta_kuni}</b> kuni",reply_markup=inline_menu
                            )
@dp.callback_query_handler(text='Toshkent')
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
  await message.message.answer(text=f"🔻 Namoz vaqtlari: <b>{region}</b>"
                            f"\n\nQuyosh - <b>{quyosh_chiqishi}</b>"
                            f"\nTong - <b>{bomdod}</b>"
                            f"\nPeshin vaqti - <b>{peshin}</b>"
                            f"\nAsr vaqti - <b>{asr}</b>"
                            f"\nShom vaqti - <b>{shom}</b>"
                            f"\nXufton vaqti - <b>{xufton}</b>"
                            f"\n\n<b>{kun} | {hijri_vaqt}</b>"
                            f"\n<b>{hijr_oy}</b>  oyning, <b>{hafta_kuni_hijri}</b> kuni"
                            f"\nHaftaning <b>{hafta_kuni}</b> kuni",reply_markup=inline_menu
                            )
@dp.callback_query_handler(text='namoz')
async def bot_echo(message: CallbackQuery):
  bomdod = f'<b>Bomdod namozi</b>\n'\
           f'Subhi sodiqdan (chin tong otgandan) kun chiqqunchadir. ' \
           f'Bomdod namozini tong yorishganda oʻqish mustahab, ' \
           f'a\'loroqdir. Soat boʻyicha hisoblansa, bomdodni kun chiqishidan 40 daqiqacha ilgari oʻqish mustahab vaqtiga muvofiq boʻladi.'
  peshin = f'<b>Pеshin namozi</b>\n' \
           f'Quyosh zavolga (og\'ishga) kеtganidan so\'ng to narsalarning soyasi quyosh tikkaga kеlgan paytdagi soyasidan tashqari oʻz uzunligiga nisbatan ikki baravar ortguniga qadar. ' \
           f'Pеshin namozini yoz faslida biroz kеchiktirib, qish faslida esa vaqti kirishi bilan oʻqish mustahabdir.'
  asr = f'<b>Asr namozi</b>\n' \
        f'Har bir narsaning soyasi quyosh tikkaga kеlgan paytdagi soyasidan tashqari oʻziga nisbatan ikki baravar ortganidan boshlab quyosh botgunchadir. ' \
        f'Asr namozini quyosh tigʻini oʻzgartirmay, nursiz holatga kirishidan oldinroq oʻqish mustahabdir.'
  shom = f'<b>Shom namozi</b>\n' \
           f'Kun botgan paytdan boshlab kunbotar tomonda shafaq (qizgʻish nurlar) gʻoyib boʻlgunchadir. ' \
           f'Shom namozini doimo quyosh botishi bilan oʻqish mustahabdir.'
  xufton = f'<b>Xufton namozi</b>\n' \
             f'Shafaq batamom yoʻqolgandan kеyin kiradi. ' \
             f'Xufton namozini kеchaning uchdan birining oxirida oʻqish afzal va nihoyatda a\'lo boʻladi.'
  vitr = f'<b>Vitr namozi</b>\n' \
           f'Xufton oʻqilgandan kеyingina kiradi. Xufton va vitr namozlarini subhi sodiqqacha oʻqisa boʻladi. ' \
           f'Vitr namozini tun oxirida uygʻonishga qodir boʻlgan kishilar subh oldidan oʻqisalar, mustahab amal qilgan boʻlishadi.'
  await message.message.answer(text=f'{bomdod}\n\n'
                                    f'{peshin}\n\n'
                                    f'{asr}\n\n'
                                    f'{shom}\n\n'
                                    f'{xufton}\n\n'
                                    f'{vitr}',reply_markup=inline_menu)




