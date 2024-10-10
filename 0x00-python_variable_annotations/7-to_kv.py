#!/usr/bin/env python3
"""
This module provides a function to create a tuple from a string
and a squared number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple from a string and the square of a number.

    Args:
        k (str): The string.
        v (Union[int, float]): The number to be squared.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string
        and the second element is the square of the number.
    """
    return (k, float(v ** 2))
