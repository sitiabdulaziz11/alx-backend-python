#!/usr/bin/env python3

"""Module that works on  Async Generator"""

from asyncio import sleep
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    coroutine that takes no arguments.
    The coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10. Use the random module.
    """
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
