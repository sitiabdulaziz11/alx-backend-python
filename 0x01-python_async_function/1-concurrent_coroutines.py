#!/usr/bin/env python3
""" Measure the runtime """


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """async routine that spawn wait_random n times with the specified max_delay.
    """

    delays = []

    process = [wait_random(max_delay) for _ in range(n)]
    result = await asyncio.gather(*process)

    for i in result:
        indx = 0
        for i, d in enumerate(delays):
            if i > d:
                index = i + 1
            else:
                break
        delays.insert(indx, i)

    return delays
