from loader import dp, db
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.types import kanal
from states.choice import Choice

@dp.message_handler(text="ð¢ Kanallar", state='*')
async def kanallar(message: types.Message, state: FSMContext):
    await message.answer("Qaysi turdagi kanaldan reklama sotib olmoqchi ekanligingizni tanlangð", reply_markup=kanal)
    await state.finish()

# IT va Texnika
@dp.message_handler(text="ð¥ IT va Texnikalar", state='*')
async def kanallar(message: types.Message, state: FSMContext):
    dannilar = db.select_kanal(slug='it')
    username = dannilar[0][1]
    kunlikpm = dannilar[0][2]
    obunachi = dannilar[0][3]
    kanalnomi = dannilar[0][4]
    type1 = dannilar[0][5]
    type2 = dannilar[0][6]
    type3 = dannilar[0][7]
    text = f"<b>ð¢ Kanal nomi</b>: {kanalnomi}\n<b>â¦ï¸ Usernamasi</b>: {username}\n<b>ð¥ Obunachilari</b>: {obunachi} ta\n<b>ð Kunlik prosmotr</b>: {kunlikpm}\n<b>âªï¸ 15/24-lik rek</b>: {type1} so'm\n<b>âªï¸ 30/24-lik rek</b>: {type2} so'm\n<b>âªï¸ 1/24-lik rek</b>: {type3} so'm"
    await message.answer(text=text)
    await state.finish()