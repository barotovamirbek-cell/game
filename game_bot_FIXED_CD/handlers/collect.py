import time
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from database import cursor, conn
from config import COLLECT_CD

router = Router()

@router.message(Command("collect"))
async def collect(msg: Message):
    uid = msg.from_user.id
    now = int(time.time())

    cursor.execute("""
    SELECT money, last_collect, house_level, car_level, clan_id
    FROM users WHERE user_id=?
    """, (uid,))
    money, last, house, car, clan_id = cursor.fetchone()

    if now - last < COLLECT_CD:
        await msg.answer(f"⏳ Подожди {COLLECT_CD - (now - last)} сек.")
        return

    income = 10 + house * 5 + car * 3

    if clan_id:
        cursor.execute("SELECT bonus FROM clans WHERE id=?", (clan_id,))
        bonus = cursor.fetchone()[0]
        income += income * bonus // 100

    cursor.execute("""
    UPDATE users SET money=money+?, last_collect=? WHERE user_id=?
    """, (income, now, uid))
    conn.commit()

    await msg.answer(f"💰 Собрано: +{income}")
