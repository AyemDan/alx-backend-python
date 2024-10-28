#!/usr/bin/env python3

def make_multiplier(multiplier: float) -> callable:
    """
    Creates a multiplier function.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        callable: A function that multiplies its input by the multiplier.
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
