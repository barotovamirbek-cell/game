from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from database import cursor

router = Router()

@router.message(Command("profile"))
async def profile(msg: Message):
    uid = msg.from_user.id

    cursor.execute(
        "SELECT balance,house_level,car_level FROM users WHERE user_id=?",
        (uid,)
    )
    bal,house,car = cursor.fetchone()

    cursor.execute(
        "SELECT clothes_rarity,clothes_bonus FROM equipped WHERE user_id=?",
        (uid,)
    )
    rarity,bonus = cursor.fetchone()

    await msg.answer(
        f"👤 Профиль\n"
        f"💰 Баланс: {bal}\n"
        f"👕 Одежда: {rarity or 'нет'} (+{bonus}%)\n"
        f"🏠 Дом: {house}\n"
        f"🚗 Машина: {car}"
    )
