from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from functions import sentiment_analysis
from database import add_record
from states import MemeState


# для связывания URL-адресов с кодом
router = Router()


@router.message(Command("sentiment"))
async def cmd_sentiment(message:Message, state: FSMContext):
    await state.set_state(MemeState.waiting_text)
    await message.answer("Напишите текст для анализа")

@router.message(MemeState.waiting_text, F.text)
async def analyze(msg:Message, state: FSMContext):
    result = await sentiment_analysis(msg.text)
    await msg.answer(f"Тональность {result}")
    add_record(msg.from_user.id, "sentiment", msg.text[:500], result)
