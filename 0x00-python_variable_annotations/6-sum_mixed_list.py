#!/usr/bin/env python3
"""Importing collection type list and Union"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list of integers and floats.

    Parameters:
    - mxd_lst (List[Union[int, float]]): The input list of integers and floats.

    Returns:
    float: The sum of the input list.
    """
    return sum(mxd_lst)
