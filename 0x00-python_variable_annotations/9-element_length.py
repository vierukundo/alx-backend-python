#!/usr/bin/env python3
"""Importing collection types List and Tuple"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the input iterable.

    Parameters:
    - lst (Iterable[Sequence]): The input iterable of sequences.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples, where each tuple contains
    a sequence from the input iterable and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
