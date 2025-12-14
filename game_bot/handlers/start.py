from aiogram import Router, types
router = Router()
@router.message(commands=['start'])
async def start(m: types.Message): await m.answer('Регистрация успешна')
