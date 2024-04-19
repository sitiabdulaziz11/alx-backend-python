#!/usr/bin/env python3
"""Calculates the length of each element in the input list.
"""

from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function that return values with the appropriate types.
    """
    return [(i, len(i)) for i in lst]
