from loader import dp
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from keyboards.default.types import types

@dp.message_handler(text="◀️ Orqaga", state='*')
async def kanallar(message: Message, state: FSMContext):
    await message.answer("<b>Qaysi biridan reklama sotib olmoqchisiz?</b>", reply_markup=types)
    await state.finish()