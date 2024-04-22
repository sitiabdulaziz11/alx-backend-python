#!/usr/bin/env python3

import asyncio

# Import the wait_random coroutine from the 0-basic_async_syntax module
wait_random = __import__('0-basic_async_syntax').wait_random

async def main():
    # Inside the main coroutine, you can call wait_random as needed
    print(await wait_random())
    print(await wait_random(5))
    print(await wait_random(15))

# Create an event loop
loop = asyncio.get_event_loop()

# Run the main coroutine within the event loop
loop.run_until_complete(main())

# Close the event loop (optional)
loop.close()

