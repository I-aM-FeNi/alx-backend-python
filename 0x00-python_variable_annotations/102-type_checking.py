#!/usr/bin/env python3
"""
This module provides a function to
zoom into an array by a given factor.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zoom into an array by a given factor.

    Args:
        lst (Tuple): The input tuple.
        factor (int): The zoom factor.

    Returns:
        List: A list where each element in the
        input tuple is repeated factor times.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)  # Changed to tuple

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Changed to integer
