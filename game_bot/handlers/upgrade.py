from aiogram import Router, types
router = Router()
@router.message(commands=['upgrade'])
async def up(m: types.Message): await m.answer('Улучшено')
