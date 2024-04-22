#!/usr/bin/env python3
""" Module that alter the code into new function"""


import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """async routine that spawn wait_random n
    times with the specified max_delay.
    """

    process = [task_wait_random(max_delay) for _ in range(n)]
    return [await proc for proc in asyncio.as_completed(process)]
