#!/usr/bin/env python3
""" module with type-annotated function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ sums a list of floats
    Args:
        input_list (list): list of floats
    Returns:
        float: the sum of floats in the list
    """
    if input_list is None:
        return 0
    else:
        return sum(input_list)
