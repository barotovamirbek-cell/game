from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

donate_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="💎 Buy donate",
                callback_data="donate_buy"
            )
        ],
        [
            InlineKeyboardButton(
                text="📦 My donate",
                callback_data="donate_my"
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
