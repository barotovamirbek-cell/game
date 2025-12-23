from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

clans_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("➕ Создать клан", callback_data="clan_create")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="menu_back")]
    ]
)
