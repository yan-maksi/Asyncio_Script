__MAIN__

Declare variables server1 and server2. These are the addresses of our 2 servers.

Declare variables input_file and output_file. These are the files to read and write.

We initialize tqdm and in total we set the number of lines in the file. 
This is a task bar so that we can see the progress, time and speed in the console.

asyncio.run(main()) - is used to run asynchronous function main. 
To call an asynchronous function from another asynchronous function, you need to write await before it,
if we are in a synchronous function or in no function, then asyncio.run()

with open(input_file, 'r') as f: - open the file with lines

for lines in f: - read each line in a loop

res = await check_line(line) - call asynchronous function that sends requests to the servers

with open(output_file, 'a') as f:
	f.write(str(res)) - open and write the result into the file


pbar.update(1) - updating the taskbar by 1

async with aiohttp.ClientSession() as session: # Create session
    async with session.get(server1, params={'word': line}) as resp: # Send request to server 1
        text1 = await resp.text() # Get response from server 1
    await asyncio.sleep(0.001) # Delay for program steel
    Async with session.get(server2, params={'word': line}) as resp: # Send request to server 2
        text2 = await resp.text() # Get response from server 2
Create a session and make 2 asynchronous requests to the server

return text1 == text2 compare answers and return the value
