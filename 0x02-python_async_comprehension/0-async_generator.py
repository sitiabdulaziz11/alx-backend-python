#!/usr/bin/env python3
"""Module that works on  Async Generator"""

import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """
    coroutine that takes no arguments.
    The coroutine will loop 10 times, each time asynchronously wait 1 second, 
    then yield a random number between 0 and 10. Use the random module.
    """
    
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(i, 10)
        