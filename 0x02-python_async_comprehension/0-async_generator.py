#!/usr/bin/env python3

"""
This module provides an asynchronous generator that yields random integers
after a delay.

Functions:
    async_generator() -> AsyncGenerator[int, None]
        Yields a random integer between 0 and 10 after a 1-second delay,
        for 10 iterations.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[int, None]:
    """
    Asynchronous generator that yields a random integer between 0 and 10 after
    a delay.

    Yields:
        int: A random integer between 0 and 10, yielded after a 1-second delay.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Wait asynchronously for 1 second
        yield random.randint(0, 10)  # Yield a random number between 0 and 10
