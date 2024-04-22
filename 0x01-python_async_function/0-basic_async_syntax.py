#!/usr/bin/env python3
""" Module that works onThe basics of async.
"""

import asyncio
import random


async def wait_random(max_delay:int=10):
    """asynchronous coroutine that takes in an integer argument  and returns after waiting for a random delay between 0 and max_delay seconds.
    Args:
        max_delay (int, optional): _description_. Defaults to 10.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
