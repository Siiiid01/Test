import asyncio
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("TG_TOKEN")

if not TOKEN:
    raise ValueError("Bot token is missing! Set it in Railway environment variables.")

dp = Dispatcher()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

START_PIC = "https://example.com/start.jpg"
START_MSG = "🔥 Welcome, {first}!\nYour ID: `{id}`\nEnjoy using this bot! 🎉"

SUCCESS_EFFECT_IDS = [
    "5104841245755180586",  # 🔥
    "5107584321108051014",  # 👍
    "5044134455711629726",  # ❤️
    "5046509860389126442",  # 🎉
]

reply_markup = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="📂 Get Files"), KeyboardButton(text="ℹ️ Help")]],
    resize_keyboard=True
)

@dp.message(commands=["start"])
async def start_command(message: Message):
    effect_id = random.choice(SUCCESS_EFFECT_IDS)  # Random effect

    await message.reply_photo(
        photo=START_PIC,
        caption=START_MSG.format(
            first=message.from_user.first_name,
            id=message.from_user.id
        ),
        reply_markup=reply_markup,
        message_effect_id=effect_id
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
