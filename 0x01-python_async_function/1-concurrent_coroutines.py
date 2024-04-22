#!/usr/bin/env python3
""" Module that execute multiple coroutines at the same time with async """


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """async routine that spawn wait_random n times with the specified max_delay.
    """

    process = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(process)]
