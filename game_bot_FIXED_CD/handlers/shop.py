from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from database import conn, cursor

router = Router()

RARITY = {
    "Common": (5, 500),
    "Rare": (10, 1500),
    "Epic": (20, 4000),
    "Legendary": (35, 10000)
}

@router.message(Command("shop"))
async def shop(msg: Message):
    text = "🛒 Магазин одежды:\n"
    for r,(b,p) in RARITY.items():
        text += f"{r} — +{b}% | {p}💰\n"
    text += "\n/buy Rare"
    await msg.answer(text)

@router.message(Command("buy"))
async def buy(msg: Message):
    uid = msg.from_user.id
    args = msg.text.split()
    if len(args) < 2 or args[1] not in RARITY:
        await msg.answer("❌ /buy Rare")
        return

    bonus,price = RARITY[args[1]]

    cursor.execute("SELECT balance FROM users WHERE user_id=?", (uid,))
    bal = cursor.fetchone()[0]
    if bal < price:
        await msg.answer("❌ Не хватает денег")
        return

    cursor.execute(
        "UPDATE users SET balance=balance-? WHERE user_id=?",
        (price, uid)
    )
    cursor.execute(
        "INSERT INTO inventory(user_id,rarity,bonus) VALUES(?,?,?)",
        (uid, args[1], bonus)
    )
    cursor.execute(
        "UPDATE equipped SET clothes_rarity=?, clothes_bonus=? WHERE user_id=?",
        (args[1], bonus, uid)
    )
    conn.commit()

    await msg.answer(f"👕 Куплено: {args[1]} (+{bonus}%)")
