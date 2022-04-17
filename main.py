import aiohttp
import asyncio
from tqdm import tqdm
from consts import my_ip1, my_ip2, delay_one_milliseconds

server1 = my_ip1
server2 = my_ip2

input_file = '370098-lines.txt'
output_file = 'output.txt'


async def check_line(line):
    # Creating a session
    async with aiohttp.ClientSession() as session:

        # Sending a request to server 1
        async with session.get(server1, params={'word': line}) as resp:
            # Getting a response from server 1
            text1 = await resp.text()

        # Delay for program stability
        await asyncio.sleep(delay_one_milliseconds)

        # Sending a request to server 2
        async with session.get(server2, params={'word': line}) as resp:
            # Getting a response from server 2
            text2 = await resp.text()

    # Comparing server responses
    return text1 == text2


async def main():
    with open(input_file, 'r') as f:
        for line in tqdm(f):
            res = await check_line(line)

            with open(output_file, 'a') as f:
                f.write(str(res))


if __name__ == "__main__":
    asyncio.run(main())
