from aiogram import types
from misc import dp,bot
import asyncio

@dp.chat_join_request_handler()
async def join(update: types.ChatJoinRequest):
    photo = open('one.jpg', 'rb')

    try:
        await update.approve()
    except:
        pass

    try:
        await asyncio.sleep(20)
        await bot.send_photo(photo = photo,caption = """<b>🩸📂5 террабайт видео с 
👧малéнькиmù👧👇</b>
Жми👉- @EkateADM 🍭
Жми👉- @EkateADM 🍭

<b>🇺🇸🎀5TB VIDEOS 💕yùng ĺaďìez💕👧👇</b>
Click👉- @EkateADM 🍭
Click👉- @EkateADM🩸""", parse_mode='html', chat_id = update.from_user.id)

    except:
        pass

    await asyncio.sleep(60)
    try:
        await bot.send_message(chat_id=update.from_user.id, text="""<b>🦄 REAL STUFF🎀
🔮Buy access - @EkateADM

🧸FIRST SEX OF SWEET GIRL👆</b>""", parse_mode='html')
    except:
        pass

