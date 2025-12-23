from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("➕ Выдать деньги", callback_data="admin_give_money")],
        [InlineKeyboardButton("➖ Забрать деньги", callback_data="admin_take_money")],
        [InlineKeyboardButton("💎 Выдать донат", callback_data="admin_give_donate")],
        [InlineKeyboardButton("📊 Статистика", callback_data="admin_stats")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="menu_back")]
    ]
)
