from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

clans_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="➕ Create clan",
                callback_data="clan_create"
            )
        ],
        [
            InlineKeyboardButton(
                text="👥 My clan",
                callback_data="clan_my"
            )
        ],
        [
            InlineKeyboardButton(
                text="⬅️ Back",
                callback_data="back_main"
            )
        ]
    ]
)
