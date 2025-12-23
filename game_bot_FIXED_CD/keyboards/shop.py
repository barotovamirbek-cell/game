from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

shop_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("🏠 Дома", callback_data="shop_house")],
        [InlineKeyboardButton("🚗 Машины", callback_data="shop_car")],
        [InlineKeyboardButton("👕 Одежда", callback_data="shop_clothes")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="menu_back")]
    ]
)

house_upgrade = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("⬆️ Улучшить дом", callback_data="upgrade_house")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="menu_back")]
    ]
)

car_upgrade = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("⬆️ Улучшить машину", callback_data="upgrade_car")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="menu_back")]
    ]
)
