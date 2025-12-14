from aiogram import Router, types
router = Router()
@router.message(commands=['collect'])
async def collect(m: types.Message): await m.answer('Сбор выполнен')
