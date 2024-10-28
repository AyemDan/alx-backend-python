#!/usr/bin/env python3

"""
This module provides a function to compute the lengths of 
elements in an iterable of sequences.

Functions:
    element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]
        Computes the length of each element and returns a list of tuples.
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Computes the length of each element in an iterable of sequences.

    Args:
        lst (Iterable[Sequence]): The iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, each containing 
        a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
