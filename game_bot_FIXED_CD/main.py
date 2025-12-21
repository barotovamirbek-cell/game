import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import start, collect, profile, shop, upgrade

async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(collect.router)
    dp.include_router(profile.router)
    dp.include_router(shop.router)
    dp.include_router(upgrade.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
