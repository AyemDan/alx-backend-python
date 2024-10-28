#!/usr/bin/env python3

"""
This module provides a function that creates a multiplier function.

Functions:
    make_multiplier(multiplier: float) -> callable
        Returns a function that multiplies its input by the specified multiplier.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that multiplies its input by the multiplier.
    """
    
    
    def multiply(n: float) -> float:
        """
        Multiplies a number by the multiplier.

        Args:
            n (float): The number to be multiplied.

        Returns:
            float: The result of the multiplication.
        """
        return n * multiplier

    return multiply
