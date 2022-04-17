import aiohttp
import asyncio
from tqdm import tqdm
from consts import MY_IP1, MY_IP2, DELAY_ONE_MILLISECONDS


async def check_line(line):
    # Creating a session
    async with aiohttp.ClientSession() as session:

        # Sending a request to server 1
        async with session.get(MY_IP1, params={'word': line}) as resp:
            # Getting a response from server 1
            text1 = await resp.text()

        # Delay for program stability
        await asyncio.sleep(DELAY_ONE_MILLISECONDS)

        # Sending a request to server 2
        async with session.get(MY_IP2, params={'word': line}) as resp:
            # Getting a response from server 2
            text2 = await resp.text()

    # Comparing server responses
    return text1 == text2


async def main():
    input_file = '370098-lines.txt'
    output_file = 'output.txt'

    with open(input_file, 'r') as f:
        for line in tqdm(f):
            res = await check_line(line)

            with open(output_file, 'a') as f:
                f.write(str(res))


if __name__ == "__main__":
    asyncio.run(main())
