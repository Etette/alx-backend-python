#!/usr/bin/env python3
"""function that multiplies a float by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Multiplies a float by multiplier
    Args:
        multiplier(float): the mulplier
    Returns:
        a function that multiples a float by
        multiplier
    """

    def multiplier_func(number: float) -> float:
        """multiplies a float by multiplier"""
        return number * multiplier

    return multiplier_func
