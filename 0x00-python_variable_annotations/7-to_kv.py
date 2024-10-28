#!/usr/bin/env python3

from typing import Tuple

def to_kv(k: str, v: float) -> Tuple[str, float]:
    """
    Converts a key and value to a tuple.

    Args:
        k (str): The key.
        v (float): The value.

    Returns:
        Tuple[str, float]: A tuple containing the key and the square of the value.
    """
    return (k, v ** 2)
