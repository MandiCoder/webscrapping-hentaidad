from modules.Client import app as bot
from modules.DownloadPhotos import DownloadPhotos
from pyrogram import filters


@bot.on_message(filters.command("start"))
def command_start(app, msg):
    msg.reply("Hola")


@bot.on_message(filters.command("run"))
def upload_images(app, msg):
    DownloadPhotos(app, f'https://hentaidad.com/popular/{1}').get_pages()



@bot.on_message()
def ver_id(app, msg):
    msg.reply( f'`{msg.chat.id}`' )
    

if __name__ == '__main__':
    print("BOT INICIADO")
    bot.run()
