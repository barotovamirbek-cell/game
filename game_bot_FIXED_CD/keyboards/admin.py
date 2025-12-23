from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="➕ Add money",
                callback_data="admin_add_money"
            ),
            InlineKeyboardButton(
                text="➖ Remove money",
                callback_data="admin_remove_money"
            )
        ],
        [
            InlineKeyboardButton(
                text="💎 Give donate",
                callback_data="admin_give_donate"
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
