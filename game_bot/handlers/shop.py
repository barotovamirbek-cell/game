from aiogram import Router, types
router = Router()
@router.message(commands=['shop'])
async def shop(m: types.Message): await m.answer('Магазин')
