#!/usr/bin/env python3
""" Duck typing sequence any"""
from typing import Any, Sequence, Union


#the types of elements of the input are not known
def safe_first_element(lst: Sequence[Any]) -> Union[Any,None]:
    """Args:
            lst: any data type
        Returns:
                None or first element
    """
    if lst:
        return lst[0]
    else:
        return None
