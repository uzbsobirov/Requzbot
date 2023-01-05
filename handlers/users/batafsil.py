from loader import dp, db
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.types import batafsil
from keyboards.inline.adminuser import adminuser

@dp.message_handler(text="📜 Batafsil", state='*')
async def kanallar(message: types.Message, state: FSMContext):
    await message.answer("Sizga yana nima qiziq?", reply_markup=batafsil)
    await state.finish()

@dp.message_handler(text="📃 Qo'llanma", state='*')
async def kanallar(message: types.Message, state: FSMContext):
    text = db.select_qollanma()[0][0]
    await message.answer(text=text, reply_markup=adminuser)
    await state.finish()

@dp.message_handler(text="📌 Shartlar", state='*')
async def kanallar(message: types.Message, state: FSMContext):
    text = db.select_shartlar()[0][0]
    await message.answer(text=text, reply_markup=adminuser)
    await state.finish()