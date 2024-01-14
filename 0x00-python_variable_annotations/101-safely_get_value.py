#!/usr/bin/env python3
"""Importing necessary modules"""
from typing import Mapping, TypeVar, Any, Union


T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary.

    Parameters:
    - dct (Mapping): The input dictionary.
    - key (Any): The key to retrieve the value from the dictionary.
    - default (Union[T, None], optional): The default value to return
    if the key is not found. Defaults to None.

    Returns:
    Union[Any, T]: The value corresponding to the key if it exists,
    otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
