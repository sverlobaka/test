def counting_sort(numbers):
    """
    >>> counting_sort([])
    []
    >>> counting_sort([2])
    [2]
    >>> counting_sort([2, 1, 1, 1, 1])
    [1, 1, 1, 1, 2]
    >>> counting_sort([1, 1, 1, 1])
    [1, 1, 1, 1]
    """
    if len(numbers) < 1:
        return numbers
    else:
        max_elem = max(numbers)
        counters = [0] * (max_elem + 1)

        for n in numbers:
            counters[n] += 1

        result = []
        for i in range(len(counters)):
            if counters[i] != 0:
                x = [i] * counters[i]
                result.extend(x)

    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
