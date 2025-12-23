from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.shop import shop_menu, house_upgrade, car_upgrade
from database import db
from config import *

router = Router()

@router.callback_query(F.callback_data == "menu_shop")
async def open_shop(call: CallbackQuery):
    await call.message.edit_text("🏪 Магазин:", reply_markup=shop_menu)

# ---- ДОМА ----
@router.callback_query(F.callback_data == "shop_house")
async def shop_house(call: CallbackQuery):
    user = db.get_user(call.from_user.id)
    lvl = user["house_lvl"]
    income = HOUSE_BASE_INCOME * lvl

    text = (
        f"🏠 Дом\n"
        f"Уровень: {lvl}\n"
        f"Доход: +{income}\n"
        f"Цена улучшения: {HOUSE_UP_PRICE * (lvl + 1)}"
    )
    await call.message.edit_text(text, reply_markup=house_upgrade)

@router.callback_query(F.callback_data == "upgrade_house")
async def upgrade_house(call: CallbackQuery):
    user = db.get_user(call.from_user.id)
    price = HOUSE_UP_PRICE * (user["house_lvl"] + 1)

    if user["balance"] < price:
        return await call.answer("❌ Недостаточно денег", show_alert=True)

    db.update_balance(call.from_user.id, -price)
    db.up_house(call.from_user.id)

    await call.answer("🏠 Дом улучшен!")

# ---- МАШИНЫ ----
@router.callback_query(F.callback_data == "shop_car")
async def shop_car(call: CallbackQuery):
    user = db.get_user(call.from_user.id)
    lvl = user["car_lvl"]

    text = (
        f"🚗 Машина\n"
        f"Уровень: {lvl}\n"
        f"Цена улучшения: {CAR_UP_PRICE * (lvl + 1)}"
    )
    await call.message.edit_text(text, reply_markup=car_upgrade)

@router.callback_query(F.callback_data == "upgrade_car")
async def upgrade_car(call: CallbackQuery):
    user = db.get_user(call.from_user.id)
    price = CAR_UP_PRICE * (user["car_lvl"] + 1)

    if user["balance"] < price:
        return await call.answer("❌ Недостаточно денег", show_alert=True)

    db.update_balance(call.from_user.id, -price)
    db.up_car(call.from_user.id)

    await call.answer("🚗 Машина улучшена!")
