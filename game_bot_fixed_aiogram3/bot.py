
import asyncio
import os
from aiogram import Bot, Dispatcher
from handlers.start import router as start_router
from handlers.collect import router as collect_router
from handlers.inventory import router as inventory_router
from handlers.upgrade import router as upgrade_router
from handlers.profile import router as profile_router
from handlers.shop import router as shop_router

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN not set")

async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(start_router)
    dp.include_router(collect_router)
    dp.include_router(inventory_router)
    dp.include_router(upgrade_router)
    dp.include_router(profile_router)
    dp.include_router(shop_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
