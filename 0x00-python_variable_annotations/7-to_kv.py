#!/usr/bin/env python3

"""
This module provides a function to convert a key and a value to a tuple, 
where the value is squared.

Functions:
    to_kv(k: str, v: float) -> Tuple[str, float]
        Returns a tuple with the key and the square of the value.
"""


from typing import List, Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts a key and value to a tuple, with the value squared.

    Args:
        k (str): The key.
        v (float): The value to be squared.

    Returns:
        Tuple[str, float]: A tuple containing the key and the square of the value.
    """
    return (k, v ** 2)
