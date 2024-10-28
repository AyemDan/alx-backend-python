#!/usr/bin/env python3

"""
This module provides an asynchronous function to wait for a random delay.

Functions:
    wait_random(max_delay: int = 10) -> float
        Waits for a random delay and returns the actual delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay.

    Args:
        max_delay (int, optional): The maximum delay in seconds.
        Defaults to 10.

    Returns:
        float: The actual delay time in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
