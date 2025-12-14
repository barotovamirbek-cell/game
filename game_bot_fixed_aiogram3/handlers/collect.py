
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("collect"))
async def collect(message: Message):
    await message.answer("Сбор выполнен")
