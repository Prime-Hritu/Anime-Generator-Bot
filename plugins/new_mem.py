from pyrogram import Client as Private_Bots
from pyrogram import filters
from database import MONGO, check_mongo
from database.members import get_all_members_ids, remove_members_id
from pyrogram.types import ChatMemberUpdated
from translation import TEXT, INLINE
from config import FORCE, SENSITIVE
from modules.enums import PicCategory, PicType
from utils.api import generate_pic
import random


@Private_Bots.on_chat_member_updated(filters.user(get_all_members_ids()))
def handle_member_update(client: Private_Bots, update: ChatMemberUpdated):
    if (
        update.new_chat_member
        and not update.old_chat_member
        and MONGO.URI
        and FORCE.FORCE_BOOL == True
    ):
        if not check_mongo() == False:
            try:
                remove_members_id(update.from_user.id)
            except:
                pass
            client.send_photo(
                chat_id=update.from_user.id,
                photo="./images/thanks.jpg",
                caption=TEXT.THANKS_FOR_JOINING.format(FORCE.CHANNEL_LINK),
            )
            type = "nsfw" if SENSITIVE.NSFW == True else "sfw"
            names: list[str] = [
                category.name
                for category in PicCategory
                if type in category.allowed_types
            ]
            category = random.choice(names)
            category_enum = PicCategory[category.upper()]
            type_enum = PicType[type.upper()]
            while True:
                try:
                    client.send_photo(
                        chat_id=update.from_user.id,
                        photo=generate_pic(type_enum, category_enum),
                        caption=TEXT.START,
                        reply_markup=INLINE.START_BOARD(),
                    )
                    break
                except Exception as e:
                    print(e)
                    continue
