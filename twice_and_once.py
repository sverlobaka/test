def twice_and_once(numbers):
    """
    >>> twice_and_once([])
    >>> twice_and_once([1, 2])
    >>> twice_and_once([1, 1])
    >>> twice_and_once([1])
    1
    >>> twice_and_once([1, 1, 2])
    2
    >>> twice_and_once([1, 2, 2])
    1
    >>> twice_and_once([1, 2, 3])
    >>> twice_and_once([1, 1, 2, 3, 3, 4, 4, 8, 8])
    2

    """

    if len(numbers) == 1:
        return numbers[0]
    elif len(numbers) == 0:
        False
    elif len(numbers) == 2:
        if numbers[:1] == numbers[1:]:
            False
    else:
        mid_numbers = len(numbers) // 2
        if numbers[mid_numbers] != numbers[mid_numbers - 1] and numbers[mid_numbers] == numbers[mid_numbers + 1]:
            return numbers[mid_numbers - 1]
        elif numbers[mid_numbers] == numbers[mid_numbers - 1] and numbers[mid_numbers] != numbers[mid_numbers + 1]:
            return numbers[mid_numbers + 1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
