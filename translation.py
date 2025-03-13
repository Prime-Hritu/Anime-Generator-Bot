from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import SENSITIVE, BOT
from config import FORCE as FORCER
from modules.enums import PicCategory


class TEXT:
    START = f"""
<b>🌸 {BOT.USERNAME}</b>
"""
    THANKS_FOR_JOINING = "<b>Thanks for joining <a href='{}'>our channel</a></b>"
    FORCE_SUB_TEXT = (
        "<b>Please Join [ </b><a href='{}'>{}</a> <b>] to continue using this bot.</b>"
    )
    BROADCAST = "<b><i>Broadcast Status:\n\nSuccess: {}\nFailed: {}</i></b>"
    FETCHING_DATABSE = "<b><i>⚙️ Fetching database...</i></b>"
    STATUS = "<b>Status:</b>\n\n<i>Total Users: {}</i>"
    STARTED = "<b>Started...</b>"


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
        BOARD.append([InlineKeyboardButton("🌺 Source Code", url=BOT.SOURCE)])
        return InlineKeyboardMarkup(BOARD)

    FORCE_SUB_BOARD = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🔈 Join Channel", url=FORCER.CHANNEL_LINK)],
        ],
    )
