def merge(a, b):
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            x = a[i]
            result.append(x)
            i += 1
        else:
            x = b[j]
            result.append(x)
            j += 1

    if j < len(b):
        result.extend(b[j:])
    else:
        result.extend(a[i:])
    return result

def merge_sort(data):
    """
    >>> merge_sort([2, 1])
    [1, 2]
    >>> merge_sort([])
    []
    """

    if len(data) < 2:
        return data

    mid_data = len(data) // 2
    left, right = data[:mid_data], data[mid_data:]
    sorted_left, sorted_right = merge_sort(left), merge_sort(right)
    return merge(sorted_left, sorted_right)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
