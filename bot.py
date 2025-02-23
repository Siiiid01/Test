import asyncio
import logging
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("TG_TOKEN")

if not TOKEN:
    raise ValueError("Bot token is missing! Set it in the environment variables.")

# Configure bot
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# Logging
logging.basicConfig(level=logging.INFO)

# Start image (Change the URL or use a local file)
START_PIC = "https://i.ibb.co/T3N3r9d/26f7a1b317fe45c561e16801a5ca1dac.jpg"

# Start message
START_MSG = """
🔥 Welcome, {first}!

Your ID: `{id}`
Enjoy using this bot! 🎉
"""

# Message Effect IDs
SUCCESS_EFFECT_IDS = [
    "5104841245755180586",  # 🔥
    "5107584321108051014",  # 👍
    "5159385139981059251",  # ❤️
    "5046509860389126442",  # 🎉
]

# Keyboard
reply_markup = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="📂 Get Files"), KeyboardButton(text="ℹ️ Help")]],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def start_command(message: Message):
    effect_id = random.choice(SUCCESS_EFFECT_IDS)  # Random effect

    await message.answer_photo(
        photo=START_PIC,
        caption=START_MSG.format(
            first=message.from_user.first_name,
            id=message.from_user.id
        ),
        reply_markup=reply_markup,
        message_effect_id=effect_id  # 🔥 Effect on message
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())