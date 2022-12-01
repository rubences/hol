#!/bin/python3

from __future__ import annotations
from collections.abc import Iterable
import math
import os
import random
import re
import sys


# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
"""Take in 2 integers, convert them to binary,
    return a binary number that is the
    result of a binary xor operation on the integers provided.
    >>> birthdayCakeCandles(25)
    '2'
    >>> birthdayCakeCandles(37)
    '0b010111'
    >>> birthdayCakeCandles(21)
    '0b01011'
    >>> birthdayCakeCandles(58)
    '0b1110011'
    >>> birthdayCakeCandles(0)
    '0b11111111'
    >>> birthdayCakeCandles(256)
    '0b000000000'
    >>> birthdayCakeCandles(-1)
    Traceback (most recent call last):
        ...
    ValueError: the value of both inputs must be positive
    >>> birthdayCakeCandles(1.1)
    Traceback (most recent call last):
        ...
    TypeError: 'float' object cannot be interpreted as an integer
    >>> birthdayCakeCandles("1")
    Traceback (most recent call last):
        ...
    TypeError: '<' not supported between instances of 'str' and 'int'
"""
    
    counter = 0
    m = max(ar)

    for i in range(0,len(ar)):
        if(ar[i] == m):
            counter += 1

    return counter


if __name__ == '__main__':
    import doctest

    # run doc test
    doctest.testmod()
