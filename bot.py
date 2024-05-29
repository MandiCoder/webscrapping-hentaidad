from modules.Client import app as bot
from modules.DownloadPhotos import DownloadPhotos
from modules.custom_server import handle
from pyrogram import filters
from pyrogram.methods.utilities.idle import idle
from aiohttp import web



@bot.on_message(filters.command("start"))
def command_start(app, msg):
    msg.reply("Hola")


@bot.on_message()
def ver_id(app, msg):
    msg.reply( f'`{msg.chat.id}`' )
    


async def run_server():
    print("SERVER INICIADO")
    server = web.Application()
    server.add_routes([web.get('/', handle)])
    runner = web.AppRunner(server)

    await runner.setup()
    await web.TCPSite(runner, host='0.0.0.0', port=8000).start()
    
    await bot.start()
    

if __name__ == '__main__':
    # bot.loop.run_until_complete(run_server())
    # idle()
    bot.start()
    DownloadPhotos(bot, f'https://hentaidad.com/').get_pages()
