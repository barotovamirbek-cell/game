
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from database import get_user, create_user

router = Router()

@router.message(Command("profile"))
async def profile_cmd(message: Message):
    uid = message.from_user.id
    if not get_user(uid):
        create_user(uid)
    u = get_user(uid)
    await message.answer(
        f"👤 Профиль\n"
        f"💰 Баланс: {u[1]}\n"
        f"📈 Доход: {u[2]} / час"
    )
