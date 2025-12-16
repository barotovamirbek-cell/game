
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from database import create_user

router = Router()

@router.message(Command("start"))
async def start_cmd(message: Message):
    create_user(message.from_user.id)
    await message.answer(
        "👋 Добро пожаловать!\n"
        "/collect — собрать доход\n"
        "/profile — профиль"
    )
