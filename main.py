import asyncio
import logging

from aiogram.methods import DeleteWebhook
from config import bot, dp


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


async def main():
    dp.include_routers(ROUTER)   # Добавить роутер
    # await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
