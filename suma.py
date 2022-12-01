def sum_ab(a, b):
    """
    Return the sum of two integers a and b
    >>> sum_ab(2, 2)
    4
    >>> sum_ab(-2, 3)
    1
    >>> sum_ab(4.9, 5.1)
    10.0
    """
    return a + b

if __name__ == '__main__':
    import doctest

    # run doc test
    doctest.testmod()