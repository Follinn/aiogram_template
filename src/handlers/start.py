from aiogram import types, Router
from aiogram.filters import Command, CommandObject
from src.keyboards import start
from aiogram import F
from src.database.db import Database as db

router = Router()


@router.message(Command('start'))
async def start_handler(msg: types.Message, command: CommandObject):
    await msg.answer('Привет')
