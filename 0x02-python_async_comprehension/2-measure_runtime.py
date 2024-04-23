#!/usr/bin/env python3
"""Run time for four parallel comprehensions """

import asyncio
from time import time
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather"""

    srt = perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    end = perf_counter()
    tot_runtm = end - srt
    return tot_runtm
