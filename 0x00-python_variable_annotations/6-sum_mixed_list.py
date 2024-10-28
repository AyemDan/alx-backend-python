#!/usr/bin/env python3

"""
This module provides a function to sum a mixed list of integers and floating-point numbers.

Functions:
    sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float
        Sums all integers and floats in a given list and returns the result as a float.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a list of integers and floating-point numbers.

    Args:
        mxd_lst (List[Union[int, float]]): The list of numbers to sum.

    Returns:
        float: The sum of the numbers in the list.
    """
    return sum(mxd_lst)
