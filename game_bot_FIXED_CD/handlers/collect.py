import time
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from database import conn, cursor

router = Router()

CD = 3600
BASE_INCOME = 100

@router.message(Command("collect"))
async def collect(msg: Message):
    uid = msg.from_user.id
    cursor.execute(
        "SELECT balance,last_collect,house_level,car_level FROM users WHERE user_id=?",
        (uid,)
    )
    bal,last,house,car = cursor.fetchone()

    cursor.execute(
        "SELECT clothes_bonus FROM equipped WHERE user_id=?",
        (uid,)
    )
    clothes = cursor.fetchone()[0]

    now = int(time.time())
    if now - last < CD:
        left = CD - (now - last)
        await msg.answer(f"⏳ Подожди {left//60} мин")
        return

    income = int(
        BASE_INCOME
        + BASE_INCOME * (house * 0.07)
        + BASE_INCOME * (car * 0.03)
        + BASE_INCOME * (clothes / 100)
    )

    cursor.execute(
        "UPDATE users SET balance=balance+?, last_collect=? WHERE user_id=?",
        (income, now, uid)
    )
    conn.commit()

    await msg.answer(f"💰 Собрано: +{income}")
