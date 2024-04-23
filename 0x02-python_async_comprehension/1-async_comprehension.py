#!/usr/bin/env python3

""" Async Comprehensions"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """coroutine that collect 10 random numbers using an async
    comprehensing over then return the 10 random numbers.
    """
    random_numbers = [num async for num in async_generator()][:10]
    return random_numbers
