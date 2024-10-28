#!/usr/bin/env python3

"""
This module provides a function to create an asyncio task that waits for
a random delay.

Functions:
    task_wait_random(max_delay: int) -> asyncio.Task
        Returns an asyncio task that runs wait_random with the
        specified maximum delay.
"""

import asyncio

# Importing the wait_random function from the basic_async_syntax module
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio task that runs wait_random with the specified
    maximum delay.

    Args:
        max_delay (int): The maximum delay for the random wait.

    Returns:
        asyncio.Task: The created asyncio task.
    """
    return asyncio.create_task(wait_random(max_delay))
