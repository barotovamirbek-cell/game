from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

back_kb = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton("⬅️ Назад", callback_data="menu_back")]]
)
