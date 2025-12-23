from aiogram import Router
from aiogram.types import CallbackQuery, Message
from database import cursor, conn

router = Router()

@router.callback_query(lambda c c.data == clan_create)
async def create(call CallbackQuery)
    await call.message.answer(✏️ Введи название клана)
    await call.answer()

@router.message()
async def clan_name(msg Message)
    if len(msg.text)  20
        return

    try
        cursor.execute(
            INSERT INTO clans (name, owner_id) VALUES (,),
            (msg.text, msg.from_user.id)
        )
        clan_id = cursor.lastrowid

        cursor.execute(
            UPDATE users SET clan_id= WHERE user_id=,
            (clan_id, msg.from_user.id)
        )
        conn.commit()

        await msg.answer(f✅ Клан {msg.text} создан)
    except
        pass
