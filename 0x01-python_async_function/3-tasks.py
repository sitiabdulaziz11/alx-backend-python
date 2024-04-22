#!/usr/bin/env python3
""" Module that do not create an async function"""


from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """Regular Function that takes an integer max_delay and
    returns a asyncio.Task."""

    process = create_task(wait_random(max_delay))

    return process
