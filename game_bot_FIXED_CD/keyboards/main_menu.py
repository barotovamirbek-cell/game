from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("💰 Collect", callback_data="do_collect"),
            InlineKeyboardButton("👤 Профиль", callback_data="menu_profile")
        ],
        [
            InlineKeyboardButton("🏪 Shop", callback_data="menu_shop"),
            InlineKeyboardButton("🏰 Clans", callback_data="menu_clans")
        ],
        [
            InlineKeyboardButton("💎 Donate", callback_data="menu_donate")
        ]
    ]
)
