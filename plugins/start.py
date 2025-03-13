from pyrogram import Client as Private_Bots
from pyrogram import filters
from pyrogram.types import Message, ChatMember, Chat
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from translation import INLINE, TEXT
from config import SENSITIVE, OWNER
from config import FORCE as FORCER
from modules.enums import PicCategory, PicType
from utils.api import generate_pic
from utils.send_reaction import send_reaction
from utils.broadcast import broadcast
from database.members import add_members_id
from database.users import get_served_users, add_served_user
import random


@Private_Bots.on_message(filters.command("status"))
def show_status(client: Private_Bots, message: Message):
    if not int(message.chat.id) == int(OWNER.ID):
        return
    msg: Message = message.reply_text(
        TEXT.FETCHING_DATABSE, reply_to_message_id=message.id
    )
    total_users = len(get_served_users())
    msg.edit(TEXT.STATUS.format(total_users))


@Private_Bots.on_message(filters.private & filters.command("broad"))
def broadcaster(c: Private_Bots, m: Message):
    if not int(m.chat.id) == int(OWNER.ID):
        return m.delete()
    m.reply_text(TEXT.START, reply_to_message_id=m.id)
    msg_to_br = m.reply_to_message
    if not msg_to_br:
        return m.reply_text("REPLY TO A MESSAGE !")
    users_list = get_served_users()
    no_sent, no_failed = broadcast(users_list, msg_to_br, m.text)
    c.send_message(
        chat_id=int(OWNER.ID), text=TEXT.BROADCAST.format(no_sent, no_failed)
    )


@Private_Bots.on_message(filters.incoming)
async def handle_message(private_bots: Private_Bots, message: Message):
    add_served_user(message.chat.id)
    if FORCER.FORCE_BOOL == True:
        FORCE = False
        try:
            got_chat_member: ChatMember = await private_bots.get_chat_member(
                FORCER.CHANNEL_USERNAME, message.chat.id
            )
            if not got_chat_member.status in [
                ChatMemberStatus.OWNER,
                ChatMemberStatus.ADMINISTRATOR,
                ChatMemberStatus.MEMBER,
            ]:
                FORCE = True
        except UserNotParticipant:
            FORCE = True
        if FORCE == True:
            chat: Chat = await private_bots.get_chat(FORCER.CHANNEL_USERNAME)
            chat_title = chat.title
            add_members_id(message.chat.id)
            return await message.reply_photo(
                photo="./images/tg.jpg",
                caption=TEXT.FORCE_SUB_TEXT.format(FORCER.CHANNEL_LINK, chat_title),
                reply_markup=INLINE.FORCE_SUB_BOARD,
            )
    send_reaction(message, "🥰")
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
