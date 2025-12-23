from aiogram import Router
from aiogram.types import CallbackQuery
from keyboards.main_menu import main_menu
from keyboards.back import back_kb
from keyboards.clans import clans_menu

router = Router()

@router.callback_query(lambda c: c.data == "menu_back")
async def back(call: CallbackQuery):
    await call.message.edit_text("🏠 Главное меню", reply_markup=main_menu)
    await call.answer()

@router.callback_query(lambda c: c.data == "menu_profile")
async def profile(call: CallbackQuery):
    await call.message.edit_text("👤 Профиль\n\nВ разработке", reply_markup=back_kb)
    await call.answer()

@router.callback_query(lambda c: c.data == "menu_clans")
async def clans(call: CallbackQuery):
    await call.message.edit_text("🏰 Кланы", reply_markup=clans_menu)
    await call.answer()

@router.callback_query(lambda c: c.data == "menu_donate")
async def donate(call: CallbackQuery):
    await call.message.edit_text("💎 Донат\n\nИспользуй /donate", reply_markup=back_kb)
    await call.answer()
