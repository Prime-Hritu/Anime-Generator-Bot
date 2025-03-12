from pyrogram import Client
from config import BOT, API, WEB
from aiohttp import web
import logging, os

routes = web.RouteTableDef()
logging.getLogger().setLevel(logging.INFO)


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
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, WEB.PORT).start()
        logging.info(f"{me.first_name} ✅✅ BOT started successfully ✅✅")

    async def stop(self, *args):
        await super().stop()
        logging.info("Bot Stopped 🙄")
        os.remove("my_app.session")


Private_Bots().run()
