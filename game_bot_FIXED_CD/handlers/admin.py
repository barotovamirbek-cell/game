from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from config import ADMIN_ID
from database import cursor, conn

router = Router()

@router.message(Command("addmoney"))
async def addmoney(msg: Message):
    if msg.from_user.id != ADMIN_ID:
        return

    _, uid, amount = msg.text.split()
    cursor.execute("UPDATE users SET money=money+? WHERE user_id=?", (int(amount), int(uid)))
    conn.commit()

    await msg.answer("✅ Готово")
