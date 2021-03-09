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
    >>> twice_and_once([1, 1, 2, 2, 3, 3, 4, 8, 8])
    4
    >>> twice_and_once([3, 3, 7, 7, 10, 11, 11])
    10
    """

    if len(numbers) == 1:
        return numbers[0]
    elif len(numbers) == 0:
        False
    elif len(numbers) == 2:
        if numbers[:1] == numbers[1:]:
            False
    elif len(numbers) == 3:
        mid_numbers = len(numbers) // 2
        if numbers[mid_numbers] != numbers[mid_numbers-1] and numbers[mid_numbers] != numbers[mid_numbers + 1]:
            pass
        elif numbers[mid_numbers] != numbers[mid_numbers-1] and numbers[mid_numbers] == numbers[mid_numbers + 1]:
            return numbers[mid_numbers-1]
        elif numbers[mid_numbers] == numbers[mid_numbers - 1] and numbers[mid_numbers] != numbers[mid_numbers + 1]:
            return numbers[mid_numbers + 1]
    else:
        mid_numbers = len(numbers) // 2
        if numbers[mid_numbers] != numbers[mid_numbers - 1] and numbers[mid_numbers] != numbers[mid_numbers + 1]:
            return numbers[mid_numbers]
        elif numbers[mid_numbers] == numbers[mid_numbers - 1] and len(numbers[:mid_numbers - 1]) % 2 == 1:
            left_find = twice_and_once(numbers[:mid_numbers - 1])
            return left_find
        elif numbers[mid_numbers] == numbers[mid_numbers + 1] and len(numbers[mid_numbers + 2:]) % 2 == 1:
            right_find = twice_and_once(numbers[mid_numbers + 2:])
            return right_find
        elif numbers[mid_numbers] == numbers[mid_numbers - 1] and len(numbers[mid_numbers + 1:]) % 2 == 1:
            right_find = twice_and_once(numbers[mid_numbers + 1:])
            return right_find
        elif numbers[mid_numbers] == numbers[mid_numbers + 1] and len(numbers[mid_numbers]) % 2 == 1:
            left_find = twice_and_once(numbers[:mid_numbers])
            return left_find

if __name__ == '__main__':
    import doctest
    doctest.testmod()
