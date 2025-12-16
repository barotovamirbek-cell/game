
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from database import get_user, create_user, collect
import time

router = Router()
CD = 3600

@router.message(Command("collect"))
async def collect_cmd(message: Message):
    uid = message.from_user.id
    if not get_user(uid):
        create_user(uid)
    collect(uid)
    await message.answer("✅ Доход собран!")
