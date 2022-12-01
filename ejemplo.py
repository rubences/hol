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
