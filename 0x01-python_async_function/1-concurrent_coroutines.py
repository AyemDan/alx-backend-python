#!/usr/bin/env python3

"""
This module provides an asynchronous function to wait for multiple
random delays.

Functions:
    wait_n(n: int, max_delay: int) -> List[float]
        Waits for n random delays, each up to max_delay, and
        returns a sorted list of the delays.
"""


import asyncio
from typing import List

# Importing the wait_random function from the basic_async_syntax module
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Waits for n random delays, each up to max_delay, and returns a sorted
    list of the delays.

    Args:
        n (int): The number of delays to wait for.
        max_delay (int): The maximum delay for each individual wait.

    Returns:
        List[float]: A sorted list of the delays.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
