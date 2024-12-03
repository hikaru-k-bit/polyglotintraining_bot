import asyncio
import logging

from app.cat import catRouter
from app.start import start
from app.utils import dp, bot


async def main() -> None:
    dp.include_routers(start, catRouter)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
