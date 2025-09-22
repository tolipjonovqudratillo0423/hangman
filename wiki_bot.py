from aiogram import Bot,Dispatcher,types
from aiogram.types import Message
from aiogram.filters import Command,CommandStart

from environs import Env 
import asyncio
import wikipedia

wikipedia.set_lang("uz")

def wiki(query):
    try:
        page = wikipedia.page(query)
        url = page.url
        result = wikipedia.summary(query,sentences=2)
        return f"TIL = UZB \n\n {result} \n\n 📎link = {url}"
    except wikipedia.exceptions.DisambiguationError as e:
        return f" Bir nechta Malumotlar topildi :{e.options[:5]}"
    except wikipedia.exceptions.PageError:
        return "Malumot topilmadi !!!"

env = Env()
env.read_env()
Wiki_bot = Bot(env.str("WIKITOKEN"))
dp=Dispatcher()

@dp.message(CommandStart())
async def command(message:Message):
    await message.answer(f"""👋 Assalomu alaykum, {message.from_user.first_name}!
🤖 Bizning Wiki_source botimizga xush kelibsiz! 🎉
🔎 Bu yerda siz kerakli ma’lumotlarni tez va oson topishingiz mumkin 📚✨
            boshalsh uchun ! '\search deb yozing' !""")

@dp.message(Command("search"))
async def search(message:types.Message):
    
    await message.answer("👋 Assalomu alaykum! Menga mavzu yuboring, men Wikipediadan ma’lumot topib beraman 📚")

@dp.message()
async def handle(messege:types.message):
    query = messege.text
    print(messege.from_user.id)
    answer = wiki(query)
    await messege.answer(answer)

async def main():
    await dp.start_polling(Wiki_bot)

    
if __name__=="__main__":
    print("Working")
    asyncio.run(main())

