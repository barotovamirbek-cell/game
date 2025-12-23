import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import start, menu, donate, clans
import database  # обязательно

async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(menu.router)
    dp.include_router(donate.router)
    dp.include_router(clans.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
