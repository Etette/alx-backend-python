#!/usr/bin/env python3
""" function that accepts mixed list of ints and floats
and returns the sum of all numbers in the list as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """accepts a mixed list of ins and floats, and returns
    the sum of all numbers in the list
    """
    return sum(mxd_lst)
