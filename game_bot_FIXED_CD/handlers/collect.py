
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from database import get_user, create_user, can_collect, collect, time_left

router = Router()

@router.message(Command("collect"))
async def collect_cmd(message: Message):
    uid = message.from_user.id

    if not get_user(uid):
        create_user(uid)

    if not can_collect(uid):
        left = time_left(uid)
        m = left // 60
        s = left % 60
        await message.answer(
            f"⏳ Рано!\n"
            f"Осталось: {m} мин {s} сек"
        )
        return

    income = collect(uid)
    await message.answer(
        f"✅ Сбор успешен!\n"
        f"+{income} 💰"
    )
