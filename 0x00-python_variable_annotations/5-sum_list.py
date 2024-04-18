#!/usr/bin/env python3
"""
annotated function sum_list which
takes a list input_list of
floats as argument and returns
their sum as a float."""


def sum_list(input_list: float) -> float:
    """annotated function that returns the sum of list.
    """
    sum = 0.0

    for i in input_list:
        sum += i

    return sum
