from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.donate import donate_kb

router = Router()

@router.message(Command("donate"))
async def donate(msg: Message):
    await msg.answer(
        "💎 Донат\n\nАвто-донат отключён\nПиши @mayserik",
        reply_markup=donate_kb
    )
