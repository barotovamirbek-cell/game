from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from keyboards.donate import donate_kb
from database import cursor

router = Router()

@router.message(Command("donate"))
async def donate(msg: Message):
    await msg.answer("💎 Донат меню", reply_markup=donate_kb)

@router.callback_query(lambda c: c.data == "donate_buy")
async def buy(call: CallbackQuery):
    await call.message.answer(
        "❌ Авто-донат отключён\n"
        "📩 Для доната пиши админу:\n@mayserik"
    )
    await call.answer()

@router.callback_query(lambda c: c.data == "donate_my")
async def my(call: CallbackQuery):
    cursor.execute(
        "SELECT crystals FROM users WHERE user_id=?",
        (call.from_user.id,)
    )
    cr = cursor.fetchone()[0]
    await call.message.answer(f"💎 У тебя {cr} доната")
    await call.answer()
