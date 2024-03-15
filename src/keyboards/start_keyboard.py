from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, WebAppInfo


def start():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='Кнопка', callback_data='butoon'))
    builder.row(InlineKeyboardButton(text='Веб приложение',
                                     web_app=WebAppInfo(url="https://follinn.github.io/march_gift/")))
    return builder.as_markup()
