import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import start, menu, collect, shop, transfer, clans, admin, donate
import database

async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(menu.router)
    dp.include_router(collect.router)
    dp.include_router(shop.router)
    dp.include_router(transfer.router)
    dp.include_router(clans.router)
    dp.include_router(admin.router)
    dp.include_router(donate.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
