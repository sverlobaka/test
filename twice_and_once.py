def twice_and_once(numbers):
    """
    >>> twice_and_once([])
    >>> twice_and_once([1, 2])
    >>> twice_and_once([1, 1])
    >>> twice_and_once([1])
    1
    >>> twice_and_once([1, 1, 2])
    2
    >>> twice_and_once([1, 1, 2, 3, 3, 4, 4, 8, 8])
    2
    >>> twice_and_once([3, 3, 7, 7, 10, 11, 11])
    10
    """

    if len(numbers) == 1:
        return numbers[0]
    elif len(numbers) < 1:
        return
    elif len(numbers) == 2:
        if numbers[:1] == numbers[1:]:
            return
    else:
        mid_numbers = len(numbers) // 2
        if numbers[mid_numbers] == numbers[mid_numbers - 1] or numbers[mid_numbers] == numbers[mid_numbers + 1]:
            left_numbers, right_numbers = numbers[:mid_numbers], numbers[mid_numbers:]
            left_part, right_part = twice_and_once(left_numbers), twice_and_once(right_numbers)
        else:
            return numbers[mid_numbers]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
