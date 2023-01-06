#!/usr/bin/env python3
"""contains a function with annotated parameters and
return values with appropraite types."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples with the length of
    each element"""
    return [(i, len(i)) for i in lst]
