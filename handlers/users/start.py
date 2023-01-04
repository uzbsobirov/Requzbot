import sqlite3

from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.types import types
from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
        await message.answer(f"<b>Assalomu Aleykum! {name}\n\nQaysi biridan reklama sotib olmoqchisiz?</b>", reply_markup=types)
        # Adminga xabar beramiz
        count = db.count_users()[0]
        msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=f"{name} bazaga oldin qo'shilgan")
        await message.answer(f"<b>Assalomu Aleykum! {name}\n\nQaysi biridan reklama sotib olmoqchisiz?</b>", reply_markup=types)
