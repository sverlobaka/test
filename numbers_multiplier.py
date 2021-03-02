def numbers_multiplier(numbers):
    """
    >>> numbers_multiplier([1, 5, 3])
    [15, 3, 5]
    >>> numbers_multiplier([1, 2, 2, 5, 8])
    [160, 80, 80, 32, 20]
    >>> numbers_multiplier([])
    []
    """

    multiplier = 1
    for char in numbers:
        multiplier *= char

    result = [int(multiplier / char) for char in numbers]
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
