from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from database import get_history


router = Router()

@router.message("history")
async def cmd_history(message:Message):
    rows = get_history(message.from_user.id)
    if not rows:
        await message.answer("история пуста")
        return
    answer = "Последние 10 действий:\n"
    for cmd, inp, res, ts in rows:
        answer+= f"- {ts[:16]} | {cmd} | {inp[:15]} \n"
    await message.answer(answer[:20])