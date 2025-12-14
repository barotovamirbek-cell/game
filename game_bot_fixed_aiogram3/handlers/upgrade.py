
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("upgrade"))
async def upgrade(message: Message):
    await message.answer("Улучшений пока нет")
