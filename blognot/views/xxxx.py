from aiohttp import web

from models.reader import FileReader


async def index(request):
    file = FileReader('blog1.md')
    return web.Response(text=file.read_content(), headers={
            "Access-Control-Allow-Origin": "*",
        })