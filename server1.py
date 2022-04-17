import random
import logger
from aiohttp import web
from consts import eighty_eighty, zero, ten

logger.loger_debug()

port = eighty_eighty

app = web.Application()


async def get_data(request):
    return web.Response(text=str(random.randint(zero, ten)))

app.router.add_get('/', get_data)

if __name__ == "__main__":
    web.run_app(app, port=port)

