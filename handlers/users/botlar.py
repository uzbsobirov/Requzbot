from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.types import kanal

@dp.message_handler(text="🤖 Botlar", state='*')
async def kanallar(message: types.Message, state: FSMContext):
    await message.answer("Qaysi turdagi botdan reklama sotib olmoqchi ekanligingizni tanlang👇", reply_markup=kanal)
    await state.finish()