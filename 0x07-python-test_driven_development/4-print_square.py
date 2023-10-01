#!/usr/bin/python3

# 4-print_square.py
"""Defines a square-prinunction."""


def print_square(size):

    """Print a square he # character.

    Args:
        size (int): The /width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
