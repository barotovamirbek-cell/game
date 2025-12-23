from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("💰 Collect", callback_data="noop")],
    [InlineKeyboardButton("🏪 Shop", callback_data="noop")],
    [InlineKeyboardButton("🏰 Clans", callback_data="noop")],
    [InlineKeyboardButton("💎 Donate", callback_data="noop")]
])
