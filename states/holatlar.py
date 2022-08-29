from aiogram.dispatcher.filters.state import State, StatesGroup


class Forma(StatesGroup):
    post_text = State()
    post_text_jonatish = State()
    post_photo = State()
    caption_photo = State()
    post_photo_jonatish = State()
    post_video = State()
    caption_video = State()
    post_video_jonatish = State()
    tasdiqlash_qabul_qilish = State()
