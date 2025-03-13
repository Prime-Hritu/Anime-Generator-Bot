from pyrogram.types import Message
import json, requests
from config import BOT


def send_reaction(message: Message, emoji: str):
    reaction = [{"type": "emoji", "emoji": emoji}]
    data = {
        "chat_id": message.chat.id,
        "message_id": message.id,
        "reaction": json.dumps(reaction),
        "is_big": False,
    }
    url = f"https://api.telegram.org/bot{BOT.TOKEN}/setMessageReaction"
    response = requests.post(url, data=data).json()
    return response["result"]
