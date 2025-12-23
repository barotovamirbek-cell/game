from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="💰 Collect",
                callback_data="do_collect"
            )
        ],
        [
            InlineKeyboardButton(
                text="🏪 Shop",
                callback_data="open_shop"
            ),
            InlineKeyboardButton(
                text="👤 Profile",
                callback_data="open_profile"
            )
        ],
        [
            InlineKeyboardButton(
                text="👥 Clans",
                callback_data="open_clans"
            ),
            InlineKeyboardButton(
                text="💎 Donate",
                callback_data="open_donate"
            )
        ]
    ]
)
