#!/usr/bin/env python3
""" a module that multiplies a float by multiplier
"""

from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
     type-annotated function make_multiplier that takes a float multiplier
     as argument and returns a function that multiplies a float by multiplier.
    """

    def fun(n: float) -> float:
        """ multiplies a float by multiplier """
        return float(n * multiplier)

    return fun
