from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from database import conn, cursor

router = Router()

@router.message(Command("start"))
async def start(msg: Message):
    uid = msg.from_user.id
    cursor.execute("INSERT OR IGNORE INTO users(user_id) VALUES(?)", (uid,))
    cursor.execute("INSERT OR IGNORE INTO equipped(user_id) VALUES(?)", (uid,))
    conn.commit()
    await msg.answer("🎮 Добро пожаловать в игру!")
