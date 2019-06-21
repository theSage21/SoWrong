from aiohttp import web
import asyncio


async def handle(request):
    response = web.Response(text=text)
    return response


app = web.Application()
app.add_routes([web.get("/", handle), web.get("/{name}", handle)])

web.run_app(app)
