#!/usr/bin/env python3
"""Importing collection type Tuple and Union"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with the first element as the string k
    and the second element as the square of the int or float v.

    Parameters:
    - k (str): The string key.
    - v (Union[int, float]): The input value, which can be either int or float.

    Returns:
    Tuple[str, float]: A tuple with the string k and the square of v.
    """
    return k, float(v ** 2)
