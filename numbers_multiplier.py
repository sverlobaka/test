def numbers_multiplier(numbers):
    """
    >>> numbers_multiplier([1, 5, 3])
    [15, 3, 5]
    >>> numbers_multiplier([1, 2, 2, 5, 8])
    [160, 80, 80, 32, 20]
    >>> numbers_multiplier([])
    []
    >>> numbers_multiplier([1, 2, 0, 5, 0])
    [0, 0, 0, 0, 0]
    >>> numbers_multiplier([1, 2, 0, 5, 8])
    [0, 0, 80, 0, 0]
    """

    zero = numbers.count(0)
    multiplier = 1
    if zero > 1:
        result = [0 * char for char in numbers]
        return result
    elif zero == 1:
        index_zero = int()
        for i, char in enumerate(numbers):
            if char != 0:
                multiplier *= char
            else:
                index_zero = i
        result = [0 * char for char in numbers]
        result[index_zero] = multiplier
        return result
    else:
        for char in numbers:
            multiplier *= char
        result = [int(multiplier / char) for char in numbers]
        return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
