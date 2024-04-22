#!/usr/bin/env python3
""" Module that Measure the runtime """

from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ function that measures the total execution
    time for wait_n(n, max_delay), and returns total_time / n"""
    start_time = time()

    run(wait_n(n, max_delay))

    end_time = time()

    return (end_time - start_time) / n
