#!/usr/bin/env python3
"""
This module provides a function to safely get a
value from a dictionary.
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Safely get a value from a dictionary.

    Args:
        dct (Mapping): The dictionary.
        key (Any): The key to look for.
        default (Union[T, None]): The default value
        if the key is not found.

    Returns:
        Union[Any, T]: The value associated with the key if it exists,
                       otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
