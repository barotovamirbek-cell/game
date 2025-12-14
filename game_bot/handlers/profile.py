from aiogram import Router, types
router = Router()
@router.message(commands=['profile'])
async def prof(m: types.Message): await m.answer('Профиль')
