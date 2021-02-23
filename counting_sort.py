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
    >>> counting_sort([-8])
    [-8]
    >>> counting_sort([2, 1, -8, 1, 0, 1, 1, -1, 3, 3, -1, 7])
    [-8, -1, -1, 0, 1, 1, 1, 1, 2, 3, 3, 7]
    """
    if len(numbers) < 1:
        return numbers
    else:
        max_elem = max(numbers)
        min_elem = min(numbers)
        positive = [0] * (max_elem + 1)
        negative = [0] * (abs(min_elem - 1))

        for n in numbers:
            if n >= 0:
                positive[n] += 1
            else:
                n = abs(n)
                negative[n] += 1

        result = []
        for i in range((len(negative) - 1), -1, -1):
            if negative[i] != 0:
                x = [i * (-1)] * negative[i]
                result.extend(x)
        for i in range(len(positive)):
            if positive[i] != 0:
                x = [i] * positive[i]
                result.extend(x)

    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
