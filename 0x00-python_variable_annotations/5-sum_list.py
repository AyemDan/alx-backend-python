#!/usr/bin/env python3

"""
This module provides a function to sum a list of floating-point numbers.

Functions:
    sum_list(input_list: List[float]) -> float
        Sums all numbers in a given list of floats and returns the result.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums a list of floating-point numbers.

    Args:
        input_list (List[float]): The list of numbers to sum.

    Returns:
        float: The sum of the numbers in the list.
    """
    return sum(input_list)
