
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("inventory"))
async def inventory(message: Message):
    await message.answer("Инвентарь пуст")
