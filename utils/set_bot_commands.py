from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("namoz_vaqtlari", "Namoz vaqtlari"),
            types.BotCommand("jonli_efir", "Jonli efirlar"),
            types.BotCommand("quron_tarjimasi", "Qur'on tarjimalari"),
            types.BotCommand("qurondan_darslar", "Qur'ondan darslar"),
            types.BotCommand("darsliklar", "Darsliklar"),
            types.BotCommand("help", "Yordam"),
        ]
    )
