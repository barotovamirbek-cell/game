from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from keyboards.main_menu import main_menu
from database import cursor, conn

router = Router()

@router.message(CommandStart())
async def start(msg: Message):
    cursor.execute(
        "INSERT OR IGNORE INTO users (user_id) VALUES (?)",
        (msg.from_user.id,)
    )
    conn.commit()

    await msg.answer(
        "🎮 Добро пожаловать в игру!\n\nВыбери действие 👇",
        reply_markup=main_menu
    )
