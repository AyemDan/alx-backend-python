#!/usr/bin/env python3

"""
This module provides a function to zoom an array by repeating its elements.

Functions:
    zoom_array(lst: Tuple, factor: int = 2) -> List
        Zooms the input tuple by repeating each element a 
        specified number of times.
"""


from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms an array by repeating its elements.

    Args:
        lst (Tuple): The input tuple.
        factor (int, optional): The zoom factor. Defaults to 2.

    Returns:
        List: The zoomed list.
    """
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
