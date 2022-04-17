from aiohttp import web
import random
import logging
logging.basicConfig(level=logging.DEBUG)

port = 8080

app = web.Application()


async def get_data(request):
    return web.Response(text=str(random.randint(0, 10)))

app.router.add_get('/', get_data)
web.run_app(app, port=port)

