import aiohttp
import asyncio
from tqdm import tqdm

server1 = "http://127.0.0.1:8080"
server2 = "http://127.0.0.1:8081"

input_file = '370098-lines.txt'
output_file = 'output.txt'

pbar = tqdm(total=370098)


async def check_line(line):
    async with aiohttp.ClientSession() as session:  # Creating a session
        async with session.get(server1, params={'word': line}) as resp:  # Sending a request to server 1
            text1 = await resp.text()  # Getting a response from server 1
        await asyncio.sleep(0.001)  # Delay for program stability
        async with session.get(server2, params={'word': line}) as resp:  # Sending a request to server 2
            text2 = await resp.text()  # Getting a response from server 2

    return text1 == text2  # Comparing server responses


async def main():
    with open(input_file, 'r') as f:
        for line in f:
            res = await check_line(line)

            with open(output_file, 'a') as f:
                f.write(str(res))

            pbar.update(1)


asyncio.run(main())
