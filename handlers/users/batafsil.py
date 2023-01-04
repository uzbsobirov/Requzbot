from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.types import batafsil

@dp.message_handler(text="📜 Batafsil", state='*')
async def kanallar(message: types.Message, state: FSMContext):
    await message.answer("Sizga yana nima qiziq?", reply_markup=batafsil)
    await state.finish()

@dp.message_handler(text="📃 Qo'llanma", state='*')
async def kanallar(message: types.Message, state: FSMContext):
    text = """<b>Botdan qanday foydalanish kerak</b>❓
              
Botdan foydalanish qiyin emas! O'zingizga kerakli turdagi reklama tanlaysiz va siz tanlagan reklama adminga boradi va admin sizga aloqaga chiqadi"""
    await message.answer(text=text)
    await state.finish()