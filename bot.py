from pyrogram import Client
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from config import BOT, API, WEB, OWNER, FORCE
from aiohttp import web
import logging, os, traceback

routes = web.RouteTableDef()
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)


async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app


@routes.get("/", allow_head=True)
async def root_route_handler(request):
    file_path = os.path.join(os.path.dirname(__file__), "web", "index.html")
    return web.FileResponse(file_path)


class Private_Bots(Client):

    def __init__(self):
        super().__init__(
            "my_app",
            API.ID,
            API.HASH,
            bot_token=BOT.TOKEN,
            plugins=dict(root="plugins"),
            workers=16,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username
        if FORCE.FORCE_BOOL == True:
            try:
                member = await self.get_chat_member(FORCE.CHANNEL_USERNAME, me.id)
                if member.status in [
                    ChatMemberStatus.OWNER,
                    ChatMemberStatus.ADMINISTRATOR,
                ]:
                    pass
            except UserNotParticipant:
                logging.info(
                    f"{me.first_name}: Bot is not admin in {FORCE.CHANNEL_USERNAME}"
                )
                await self.send_message(
                    chat_id=int(OWNER.ID),
                    text=f"{me.first_name}: Bot is not admin in {FORCE.CHANNEL_USERNAME}",
                )
                await super().stop()
                return
            except Exception:
                logging.info(
                    f"❌❌ {me.first_name}: Error occoured while starting\n\n{str(traceback.format_exc())}"
                )
                await self.send_message(
                    chat_id=int(OWNER.ID),
                    text=f"❌❌ {me.first_name}: Error occoured while starting\n\n{str(traceback.format_exc())}",
                )
                await super().stop()
                return
        await self.send_message(
            chat_id=int(OWNER.ID),
            text=f"{me.first_name} ✅✅ BOT started successfully ✅✅",
        )
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        self.site = web.TCPSite(app, bind_address, WEB.PORT)
        await self.site.start()
        logging.info(f"{me.first_name} ✅✅ BOT started successfully ✅✅")

    async def stop(self, *args):
        await self.site.stop()
        await super().stop()
        logging.info("Bot Stopped 🙄")
        os.remove("my_app.session")


Private_Bots().run()
