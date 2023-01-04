from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext

@dp.message_handler(text="👥 Guruhlar", state='*')
async def kanallar(message: types.Message, state: FSMContext):
    await message.answer("Bu bo'limda hali guruhlar yo'q!")
    await state.finish()