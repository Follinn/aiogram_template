from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv

load_dotenv()


TOKEN: str = os.getenv("TOKEN")
admin_id = ['710580176']
chanel_id = -1002110755049
DataBaseCon = os.getenv("DataBaseCon")

bot = Bot(token=TOKEN)
# Диспетчер
dp = Dispatcher()