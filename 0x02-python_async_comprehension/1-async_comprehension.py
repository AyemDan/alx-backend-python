#!/usr/bin/env python3

"""
This module provides an asynchronous function using comprehension to
collect values from an async generator.

Functions:
    async_comprehension() -> List[float]
        Collects numbers generated by async_generator into a list
        using async comprehension.
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects numbers generated by async_generator into a list using
    async comprehension.

    Returns:
        List[float]: A list of numbers generated asynchronously.
    """
    return [number async for number in async_generator()]
