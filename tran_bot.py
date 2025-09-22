from aiogram import Bot,Dispatcher
from aiogram.types import Message
from aiogram.filters import Command , CommandStart

from environs import Env 
import asyncio
from deep_translator import GoogleTranslator

env = Env()
env.read_env()
bot = Bot(env.str("TRANTOKEN"))
dp=Dispatcher()

@dp.message(CommandStart())
async def command(message:Message):
    await message.answer(f"""👋 Assalomu alaykum, {message.from_user.first_name}!
🤖 Bizning Translate botimizga xush kelibsiz! 🎉
🔎 Bu yerda siz kerakli ma’lumotlarni tez va oson Tarjima Qilishingiz mumkin 📚✨
        boshalsh uchun ! '\\search deb yozing""")
    
async def tran(message: Message):
    if not message.text:
        await message.reply(" Iltimos, faqat matn yuboring.")
        return 
@dp.message()
async def tran(message:Message):
    
    translated = GoogleTranslator(source="uz",target="en").translate(message.text)

    await message.reply(f"--> {message.text} Tarjimasi --> {translated}")

    
async def main():
    print("Tran Bot Working ✅")
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())
    
    


    

