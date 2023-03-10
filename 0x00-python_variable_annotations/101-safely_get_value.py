#!/usr/bin/env python3
"""Duck Typing Typevar"""
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None)\
        -> Union[Any, T]:
    """Args:
            dct: mapping
            key: any data type
            default: default value
        Returns:
            Any or T format
    """
    if key in dct:
        return dct[key]
    else:
        return default
