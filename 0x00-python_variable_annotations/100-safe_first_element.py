#!/usr/bin/env python3

"""
This module provides a function to safely retrieve the first element of a sequence.

Functions:
    safe_first_element(lst: Sequence[Any]) -> Union[Any, None]
        Retrieves the first element of the sequence, returning None if the sequence is empty.
"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely retrieves the first element of a sequence.

    Args:
        lst (Sequence[Any]): The sequence from which to retrieve the first element.

    Returns:
        Union[Any, None]: The first element if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    return None
