from aiohttp import web

async def handle(request):
    return web.Response(text="<h1>Hola Mundoooo</h1>")