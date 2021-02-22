def counting_sort(numbers):
    """
    >>> counting_sort([])
    []
    >>> counting_sort([2])
    [2]
    >>> counting_sort([2, 1, 1, 1, 1])
    [1, 1, 1, 1, 2]
    """
    if len(numbers) < 1:
        return numbers
    else:
        max_elem = max(numbers)
        counters = [0] * (max_elem + 1)

        for n in numbers:
            counters[n] += 1

        pos = 0
        for i in range(len(counters)):
            for j in range(counters[i]):
                numbers[pos] = i
                pos += 1

    return numbers

if __name__ == '__main__':
    import doctest
    doctest.testmod()
