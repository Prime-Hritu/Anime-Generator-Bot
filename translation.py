from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import SENSITIVE, BOT
from modules.enums import PicCategory


class TEXT:
    START = f"""
<b>🌸 {BOT.USERNAME}</b>
"""


class INLINE:
    def START_BOARD():
        type = "nsfw" if SENSITIVE.NSFW == True else "sfw"
        BOARD = []
        names: list[str] = [
            category.name for category in PicCategory if type in category.allowed_types
        ]
        zipped_name = zip(names[::2], names[1::2])
        for name1, name2 in zipped_name:
            BOARD.append(
                [
                    InlineKeyboardButton(
                        name1.capitalize(), callback_data=f"{type}_{name1.lower()}"
                    ),
                    InlineKeyboardButton(
                        name2.capitalize(), callback_data=f"{type}_{name2.lower()}"
                    ),
                ]
            )
        return InlineKeyboardMarkup(BOARD)
