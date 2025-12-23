from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

clans_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("➕ Создать клан", callback_data="clan_create")],
        [InlineKeyboardButton("👥 Мой клан", callback_data="clan_my")],
        [InlineKeyboardButton("🏆 Топ кланов", callback_data="clan_top")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="menu_back")]
    ]
)
