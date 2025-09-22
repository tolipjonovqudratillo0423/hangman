from aiogram import Bot,Dispatcher
from aiogram.types import Message
from environs import Env 
import asyncio

env = Env()
env.read_env()
bot = Bot(env.str("TOKEN"))
dp=Dispatcher()

@dp.message()
async def echo(message:Message):
    print(message.from_user.id,"--->" ,message.from_user.first_name, "=" , message.text)
    await message.reply(f"Assalomu Alaykum :{message.from_user.first_name} , \n Siz {message.text} yozdingiz !!!")
async def main():
    print("Working")
    await dp.start_polling(bot)
    
asyncio.run(main())



