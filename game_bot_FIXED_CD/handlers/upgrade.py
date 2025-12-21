from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from database import conn, cursor

router = Router()

@router.message(Command("upgrade_house"))
async def house(msg: Message):
    uid = msg.from_user.id
    cursor.execute("SELECT house_level,balance FROM users WHERE user_id=?", (uid,))
    lvl,bal = cursor.fetchone()
    price = 500 * lvl * lvl
    if bal < price:
        await msg.answer(f"❌ Нужно {price}")
        return
    cursor.execute(
        "UPDATE users SET balance=balance-?, house_level=house_level+1 WHERE user_id=?",
        (price, uid)
    )
    conn.commit()
    await msg.answer(f"🏠 Дом → {lvl+1}")

@router.message(Command("upgrade_car"))
async def car(msg: Message):
    uid = msg.from_user.id
    cursor.execute("SELECT car_level,balance FROM users WHERE user_id=?", (uid,))
    lvl,bal = cursor.fetchone()
    price = 800 * lvl * lvl
    if bal < price:
        await msg.answer(f"❌ Нужно {price}")
        return
    cursor.execute(
        "UPDATE users SET balance=balance-?, car_level=car_level+1 WHERE user_id=?",
        (price, uid)
    )
    conn.commit()
    await msg.answer(f"🚗 Машина → {lvl+1}")
