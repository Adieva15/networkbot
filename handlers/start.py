from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start(message:Message):
    text =("Hello! Я нейросетевой бот.\n"
        "Мои команды:\n"
        "/start\n"
        "/help\n"
        "/sentiment\n"
        "/history\n")
    await message.answer(text)
