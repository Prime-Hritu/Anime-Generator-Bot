from dotenv import load_dotenv

load_dotenv()  # This will load the variables from .env into os.environ

import os
from UserAgentReplica import UserAgent


class BOT:
    """
    TOKEN: Bot token generated from @BotFather
    USERNAME: Username of the bot with @
    SOURCE: Source code's url of the bot
    """

    TOKEN = os.environ.get("TOKEN", "")
    USERNAME = "@AIanimeGenBot"
    SOURCE = "https://github.com/prime-hritu/Anime-Generator-Bot"


class API:
    """
    HASH: Telegram API hash from https://my.telegram.org
    ID = Telegram API ID from https://my.telegram.org
    """

    HASH = os.environ.get("API_HASH", "")
    ID = int(os.environ.get("API_ID", 0))


class MONGO:
    """
    URI: MongoDB Url (optional)
    NAME: MongoDB collection name (optional)
    """

    URI = os.environ.get(
        "MONGO_URI",
        "mongodb+srv://pateva6668:Tr9jnT8Yy5YFj2ij@cluster0.b8mgv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    )
    NAME = os.environ.get("MONGO_NAME", "AnimeBot")


class FORCE:
    """
    CHANNEL_LINK: Force sub channel link as url.
    CHANNEL_USERNAME: Force sub channel username with @
    """

    FORCE_SUB = os.environ.get("FORCE", "")
    FORCE_BOOL = True if str(FORCE_SUB).lower() == "true" else False
    CHANNEL_LINK = os.environ.get("CHANNEL_LINK", "")  # https://t.me/Private_Bots
    CHANNEL_USERNAME = os.environ.get(
        "CHANNEL_USERNAME", ""
    )  # with @ ( @Private_Bots )


class OWNER:
    """
    ID: Owner's user id, get it from @userinfobot
    """

    ID = int(os.environ.get("OWNER", 0))


class URL:
    """
    ❌ DON'T TOUCH THIS ⚠️
    """

    API = "https://api.waifu.pics/{type}/{category}"
    HEARDERS = {"User-Agent": UserAgent().chrome()}


class WEB:
    """
    PORT: Specific port no. on which you want to run your bot, DON'T TOUCH IT IF YOU DON'T KNOW WHAT IS IT.
    """

    PORT = int(os.environ.get("PORT", 8000))  # 8000 port for koyeb


class SENSITIVE:
    """
    NSFW: False if you don't want bot to give 18+ pics or gif.
          True means extremly and only 18+ (NSFW) contents.
    """

    NSFW = True if str(os.environ.get("NSFW", "false")).lower() == "true" else False
