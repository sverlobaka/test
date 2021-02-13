def merge_sort(data):
    """
    >>> merge_sort([22, 5, 1, 23, 6, 55, 89, 23, 15, 98, 9, 40, 9, 44, 3, 9, 12, 67, 87, 43, 90])
    [1, 3, 5, 6, 9, 9, 9, 12, 15, 22, 23, 23, 40, 43, 44, 55, 67, 87, 89, 90, 98]
    >>> merge_sort([2, 1])
    [1, 2]
    >>> merge_sort([])
    []
    >>> merge_sort([1, 0, 45, 3])
    [0, 1, 3, 45]
    >>> merge_sort([99, -6, 1, 23, -1, 40, 9, 5, 9999999999])
    [-6, -1, 1, 5, 9, 23, 40, 99, 9999999999]
    >>> merge_sort([99, -6, 1, 23, 3.5, 0, -3.5,-1, 40, 9, 5, 9999999999])
    [-6, -3.5, -1, 0, 1, 3.5, 5, 9, 23, 40, 99, 9999999999]
    """

    if len(data) > 2:
        list_index = len(data) - 1

        for i in range(list_index):
            min_value = data[i]
            min_index = i

            for j in range(i + 1, list_index + 1):
                if min_value > data[j]:
                    min_value = data[j]
                    min_index = j

            if min_index != i:
                data[i], data[min_index] = data[min_index], data[i]

    elif len(data) == 2 and data[0] > data [1]:
        data[0], data[1] = data[1], data[0]

    return data

if __name__ == '__main__':
    import doctest
    doctest.testmod()
