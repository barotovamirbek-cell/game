
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("shop"))
async def shop(message: Message):
    await message.answer("Магазин")
