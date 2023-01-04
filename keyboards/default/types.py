from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

types = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📢 Kanallar"),
            KeyboardButton(text="👥 Guruhlar")
        ],
        [
            KeyboardButton(text="🤖 Botlar")
        ],
        [
            KeyboardButton(text="📜 Batafsil")
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)

# Kanallardan reklama
kanal = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎵 Musiqa"),
            KeyboardButton(text="🌙 Islomiy")
        ],
        [
            KeyboardButton(text="😹 Kongilochar"),
            KeyboardButton(text="📹 Qora videolar")
        ],
        [
            KeyboardButton(text="🖥 IT va Texnikalar"),
            KeyboardButton(text="⚽️ Sport")
        ],
        [
            KeyboardButton(text="🗞 Yangilik"),
            KeyboardButton(text="👤 Shaxsiy blog")
        ],
        [
            KeyboardButton(text="◀️ Orqaga")
        ]
    ], 
    resize_keyboard=True, one_time_keyboard=True
)

# Botlardan reklama
kanal = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🖥 IT va Texnikalar"),
            KeyboardButton(text="🎵 Musiqa")
        ],
        [
            KeyboardButton(text="🖼 Logo"),
            KeyboardButton(text="📥 Yuklovchi")
        ],
        [
            KeyboardButton(text="💥 Turfa bot"),
            KeyboardButton(text="🎁 Konkurs")
        ],
        [
            KeyboardButton(text="◀️ Orqaga")
        ]
    ], 
    resize_keyboard=True, one_time_keyboard=True
)