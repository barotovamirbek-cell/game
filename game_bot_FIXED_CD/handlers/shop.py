from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from database import cursor, conn

router = Router()

@router.message(Command("shop"))
async def shop(msg: Message):
    await msg.answer(
        "🏪 Магазины:\n"
        "🏠 /buy_house\n"
        "🚗 /buy_car"
    )

@router.message(Command("buy_house"))
async def buy_house(msg: Message):
    uid = msg.from_user.id
    cursor.execute("SELECT house_level, money FROM users WHERE user_id=?", (uid,))
    lvl, money = cursor.fetchone()

    price = (lvl + 1) * 100
    if money < price:
        await msg.answer("❌ Недостаточно денег")
        return

    cursor.execute("""
    UPDATE users SET house_level=house_level+1, money=money-?
    WHERE user_id=?
    """, (price, uid))
    conn.commit()

    await msg.answer(f"🏠 Дом улучшен до {lvl+1} уровня за {price}")
