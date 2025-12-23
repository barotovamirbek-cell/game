from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Главное меню магазина
shop_menu = InlineKeyboardMarkup(row_width=2)
shop_menu.add(
    InlineKeyboardButton(text="🏠 Дом", callback_data="shop_house"),
    InlineKeyboardButton(text="🚗 Машина", callback_data="shop_car")
)
shop_menu.add(
    InlineKeyboardButton(text="👕 Одежда", callback_data="shop_clothes")
)
shop_menu.add(
    InlineKeyboardButton(text="⬅️ Назад", callback_data="back_main")
)

# Клавиатура улучшения дома
house_upgrade = InlineKeyboardMarkup(row_width=1)
house_upgrade.add(
    InlineKeyboardButton(text="⬆️ Улучшить дом", callback_data="upgrade_house"),
    InlineKeyboardButton(text="🔙 Назад", callback_data="shop_house")
)

# Клавиатура улучшения машины
car_upgrade = InlineKeyboardMarkup(row_width=1)
car_upgrade.add(
    InlineKeyboardButton(text="⬆️ Улучшить машину", callback_data="upgrade_car"),
    InlineKeyboardButton(text="🔙 Назад", callback_data="shop_car")
)
