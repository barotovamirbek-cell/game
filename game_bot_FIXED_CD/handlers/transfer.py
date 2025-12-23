import time
from aiogram import Router
from aiogram.types import Message
from database import cursor, conn
from config import TRANSFER_CD

router = Router()

@router.message(lambda m: m.text.startswith("+му"))
async def transfer(msg: Message):
    if not msg.reply_to_message:
        await msg.answer("❗ Используй команду ответом на сообщение")
        return

    amount = int(msg.text.split()[1])
    if amount < 1:
        return

    uid = msg.from_user.id
    to_id = msg.reply_to_message.from_user.id
    now = int(time.time())

    cursor.execute("SELECT money, last_transfer FROM users WHERE user_id=?", (uid,))
    money, last = cursor.fetchone()

    if now - last < TRANSFER_CD or money < amount:
        return

    cursor.execute("UPDATE users SET money=money-?, last_transfer=? WHERE user_id=?", (amount, now, uid))
    cursor.execute("UPDATE users SET money=money+? WHERE user_id=?", (amount, to_id))
    conn.commit()

    await msg.answer(f"✅ Переведено {amount}")
