from pyrogram import Client as Private_Bots
from pyrogram import filters
from pyrogram.types import Message
from translation import INLINE, TEXT
from config import SENSITIVE
from modules.enums import PicCategory, PicType
from utils.api import generate_pic
import random


@Private_Bots.on_message(filters.incoming)
async def handle_message(private_bots: Private_Bots, message: Message):
    type = "nsfw" if SENSITIVE.NSFW == True else "sfw"
    names: list[str] = [
        category.name for category in PicCategory if type in category.allowed_types
    ]
    category = random.choice(names)
    category_enum = PicCategory[category.upper()]
    type_enum = PicType[type.upper()]
    while True:
        try:
            await message.reply_photo(
                photo=generate_pic(type_enum, category_enum),
                caption=TEXT.START,
                reply_markup=INLINE.START_BOARD(),
            )
            break
        except Exception as e:
            print(e)
            continue
