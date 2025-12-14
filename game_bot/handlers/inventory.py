from aiogram import Router, types
router = Router()
@router.message(commands=['inventory'])
async def inv(m: types.Message): await m.answer('Инвентарь пуст')
