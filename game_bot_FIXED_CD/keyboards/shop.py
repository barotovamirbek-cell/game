from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

shop_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🏠 Houses",
                callback_data="shop_houses"
            ),
            InlineKeyboardButton(
                text="🚗 Cars",
                callback_data="shop_cars"
            )
        ],
        [
            InlineKeyboardButton(
                text="👕 Clothes",
                callback_data="shop_clothes"
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
