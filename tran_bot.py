from aiogram import Bot,Dispatcher
from aiogram.types import Message
from aiogram.filters import Command , CommandStart

from environs import Env 
import asyncio
from deep_translator import GoogleTranslator

env = Env()
env.read_env()
bot = Bot(env.str("TOKEN"))
dp=Dispatcher()
async def tran(query):
    return GoogleTranslator(query,"en")

@dp.message(CommandStart())
async def command(message:Message):
    await message.answer(f"""👋 Assalomu alaykum, {message.from_user.first_name}!
🤖 Bizning Translate botimizga xush kelibsiz! 🎉
🔎 Bu yerda siz kerakli ma’lumotlarni tez va oson Tarjima Qilishingiz mumkin 📚✨
        boshalsh uchun ! '\search deb yozing""")
dp.message()
async def tran(message:Message):
    
    translated = GoogleTranslator(source="uz",target="eng").translate(message.text)

    await message.reply(f"--> {message.text} Tarjimasi --> {translated}")

    
async def main():
    await dp.start_polling(bot)
    print("Tran Bot Working")

if __name__=="__main__":
    asyncio.run(main())
    
    


    

