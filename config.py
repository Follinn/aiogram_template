from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv

load_dotenv()


TOKEN: str = os.getenv("TOKEN")
admin_id = [admin id]
chanel_id = -100000000
DataBaseCon = os.getenv("DataBaseCon")

bot = Bot(token=TOKEN)
# Диспетчер
dp = Dispatcher()
