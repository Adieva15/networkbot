import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from config import BOT_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message:Message):
    await message.answer(
        "Hello!\n"
        "/start, 'help"
    )

@dp.message(F.text)
async def echo(message:Message):
    await message.answer(f"{message.text}")

@dp.message(F.sticker)
async def echo_sticker(message: Message):
    await message.answer_sticker(sticker=message.sticker.file_id)

@dp.message(F.photo)
async def echo_photo(message:Message):
    photo = message.photo[-1]
    await message.answer_photo(photo.file_id, caption=message.caption)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())