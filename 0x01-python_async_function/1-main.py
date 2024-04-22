#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

async def main():
    print(await wait_n(5, 5))
    print(await wait_n(10, 7))
    print(await wait_n(10, 0))

loop = asyncio.get_event_loop()

# Run the main coroutine within the event loop
loop.run_until_complete(main())

# Close the event loop (optional)
loop.close()