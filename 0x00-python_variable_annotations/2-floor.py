#!/usr/bin/env python3

"""
This module provides a function to calculate the floor 
of a floating-point number.

Functions:
    floor(n: float) -> int
        Returns the floor of a given floating-point number.
"""


import math


def floor(n: float) -> int:
    """
    Returns the floor of a floating-point number.

    Args:
        n (float): The number to floor.

    Returns:
        int: The floor of the number.
    """
    return math.floor(n)
