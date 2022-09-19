from aiogram import Bot, Dispatcher, executor, types
import asyncio
import aioschedule


bot = Bot(token='5602209708:AAGyWRSIB_9T78fFVuR3LdwmfD4hq97Tr8g')
dp = Dispatcher(bot)


@dp.message_handler()
async def welcome(message: types.Message):
    await message.reply("hey... i am your SSBT Bot and i am working only for A section Students")


async def AI_lecture():
    await bot.send_message(-1001622926756,".\n\n\n🛑🛑🛑Get ready for AI_lecture🛑🛑🛑\n\n👇🏻👇🏻Use bot to download notes📚👇🏻👇🏻\n\n👉🏻📚👉🏻https://t.me/pagal43_bot👈🏻📚👈🏻")


async def DBMS_lecture():
    await bot.send_message(-1001622926756,'.\n\n\n🛑🛑🛑Get ready for DBMS_lecture🛑🛑🛑\n\n👇🏻👇🏻Use bot to download notes📚👇🏻👇🏻\n\n👉🏻📚👉🏻https://t.me/pagal43_bot👈🏻📚👈🏻')


async def CLE_lecture():
    await bot.send_message(-1001622926756,'.\n\n\n🛑🛑🛑Get ready for CLE_lecture🛑🛑🛑\n\n👇🏻👇🏻Use bot to download notes📚👇🏻👇🏻\n\n👉🏻📚👉🏻https://t.me/pagal43_bot👈🏻📚👈🏻')


async def SE_lecture():
    await bot.send_message(-1001622926756,'.\n\n\n🛑🛑🛑Get ready for SE_lecture🛑🛑🛑\n\n👇🏻👇🏻Use bot to download notes📚👇🏻👇🏻\n\n👉🏻📚👉🏻https://t.me/pagal43_bot👈🏻📚👈🏻')


async def FLAT_lecture():
    await bot.send_message(-1001622926756,'.\n\n\n🛑🛑🛑Get ready for FLAT_lecture🛑🛑🛑\n\n👇🏻👇🏻Use bot to download notes📚👇🏻👇🏻\n\n👉🏻📚👉🏻https://t.me/pagal43_bot👈🏻📚👈🏻')


async def MON_prac():
    await bot.send_message(962909870,'.\n\n\n🛑🛑🛑A1 WPL-PKP-LAB-7\nA2 SEL-ATB-LAB-5\nA3 DBMSL-KPA-LAB-10🛑🛑🛑\n\n👇🏻👇🏻Use bot to download notes📚👇🏻👇🏻\n\n👉🏻📚👉🏻https://t.me/pagal43_bot👈🏻📚👈🏻')


async def TUE_prac():
    await bot.send_message(962909870,'.\n\n\n🛑🛑🛑A1 SEL-ATB-LAB-5\nA2 DBMSL-KPA-LAB-10\nA3 WPL-PKP-LAB-7🛑🛑🛑\n\n👇🏻👇🏻Use bot to download notes📚👇🏻👇🏻\n\n👉🏻📚👉🏻https://t.me/pagal43_bot👈🏻📚👈🏻')


async def Wed_prac():
    await bot.send_message(962909870,'.\n\n\n🛑🛑🛑A1 DBMSL-KPA-LAB-10\nA2 WPL-PKP-LAB-7\nA3 SEL-ATB-LAB-5🛑🛑🛑\n\n👇🏻👇🏻Use bot to download notes📚👇🏻👇🏻\n\n👉🏻📚👉🏻https://t.me/pagal43_bot👈🏻📚👈🏻')


async def T_G():
    await bot.send_message(962909870, '.\n\n\n🛑🛑🛑Get ready for Teacher Gurdian meet🛑🛑🛑')


#async def tifin_jevan():
#   await bot.send_dice(-1001622926756, emoji="🎲")
#  await bot.send_message(962909870, '.\n\n\nGet ready for lunch🍲🌮🍝🍜\n\n\n.')


async def scheduler():
    # Every sunday

    # Every monday
    aioschedule.every().monday.at("10:50").do(AI_lecture)
    aioschedule.every().monday.at("11:50").do(DBMS_lecture)
    #aioschedule.every().monday.at("13:00").do(tifin_jevan)
    aioschedule.every().monday.at("13:35").do(MON_prac)
    aioschedule.every().monday.at("15:35").do(CLE_lecture)
    aioschedule.every().monday.at("16:35").do(SE_lecture)

    # Every tuesday
    aioschedule.every().tuesday.at("10:50").do(TUE_prac)
    #aioschedule.every().tuesday.at("13:00").do(tifin_jevan)
    aioschedule.every().tuesday.at("13:35").do(SE_lecture)
    aioschedule.every().tuesday.at("14:35").do(FLAT_lecture)
    aioschedule.every().tuesday.at("15:35").do(CLE_lecture)
    aioschedule.every().tuesday.at("16:35").do(DBMS_lecture)

    # Every Wednesday
    aioschedule.every().wednesday.at("10:50").do(Wed_prac)
    #aioschedule.every().wednesday.at("13:00").do(tifin_jevan)
    aioschedule.every().wednesday.at("13:35").do(CLE_lecture)
    aioschedule.every().wednesday.at("14:35").do(DBMS_lecture)
    aioschedule.every().wednesday.at("15:35").do(FLAT_lecture)

    # Every Thursday

    # Every Friday
    aioschedule.every().friday.at("10:50").do(FLAT_lecture)
    aioschedule.every().friday.at("11:50").do(SE_lecture)
    #aioschedule.every().friday.at("13:00").do(tifin_jevan)
    aioschedule.every().friday.at("13:35").do(AI_lecture)

    # Every Saturday
    aioschedule.every().saturday.at("10:50").do(DBMS_lecture)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    asyncio.create_task(scheduler())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)