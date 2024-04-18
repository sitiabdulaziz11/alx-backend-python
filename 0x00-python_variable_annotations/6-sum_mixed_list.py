#!/usr/bin/env python3
"""
type-annotated function sum_mixed_list which takes a list mxd_lst
of integers and floats
and returns their sum as a float.
"""


from typing import Union


def sum_mixed_list(mxd_lst: Union[int, float]) -> float:
    """annotated function that returns the sum of list.
    """

    sum = 0.0

    for i in mxd_lst:
        sum += i

    return sum
