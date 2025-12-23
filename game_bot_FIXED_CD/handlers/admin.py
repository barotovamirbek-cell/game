from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from config import ADMIN_ID
from keyboards.admin import admin_menu
from database import db

router = Router()

def is_admin(user_id: int) -> bool:
    return user_id == ADMIN_ID

@router.message(F.text == "/admin")
async def admin_cmd(msg: Message):
    if not is_admin(msg.from_user.id):
        return
    await msg.answer("🔧 Админ панель", reply_markup=admin_menu)

@router.callback_query(F.callback_data == "admin_stats")
async def admin_stats(call: CallbackQuery):
    if not is_admin(call.from_user.id):
        return

    users = db.count_users()
    await call.message.edit_text(f"📊 Пользователей: {users}", reply_markup=admin_menu)
