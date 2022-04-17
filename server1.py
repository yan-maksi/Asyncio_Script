import random
import logger
from aiohttp import web
from consts import EIGHTY_EIGHTY, ZERO, TEN

logger.loger_debug()

port = EIGHTY_EIGHTY

app = web.Application()


async def get_data(request):
    return web.Response(text=str(random.randint(ZERO, TEN)))

app.router.add_get('/', get_data)

if __name__ == "__main__":
    web.run_app(app, port=port)

