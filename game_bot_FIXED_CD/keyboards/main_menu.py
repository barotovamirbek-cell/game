from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("👤 Профиль", callback_data="menu_profile"),
            InlineKeyboardButton("🏰 Кланы", callback_data="menu_clans")
        ],
        [
            InlineKeyboardButton("💎 Донат", callback_data="menu_donate")
        ]
    ]
)
