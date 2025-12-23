from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from database import cursor, conn
from keyboards.main_menu import main_menu

router = Router()

@router.message(CommandStart())
async def start(msg: Message):
    cursor.execute(
        "INSERT OR IGNORE INTO users (user_id) VALUES (?)",
        (msg.from_user.id,)
    )
    conn.commit()

    await msg.answer("🎮 Главное меню", reply_markup=main_menu)
