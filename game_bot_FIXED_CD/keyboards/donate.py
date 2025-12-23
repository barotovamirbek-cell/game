from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

donate_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("💎 Купить донат", callback_data="donate_buy")],
        [InlineKeyboardButton("📦 Мой донат", callback_data="donate_my")]
    ]
)
