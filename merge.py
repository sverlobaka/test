def merge(intervals):
    """
    See https://leetcode.com/problems/merge-intervals/
    >>> merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    [[1, 6], [8, 10], [15, 18]]
    >>> merge([[1, 4], [4, 5]])
    [[1, 5]]
    >>> merge([[1, 4]])
    [[1, 4]]
    >>> merge([[1, 3], [2, 6], [8, 10], [15, 18], [1, 7], [3, 5], [10, 16]])
    [[1, 7], [8, 18]]
    """
    intervals.sort()
    result = [intervals[0]]
    for a, b in intervals[1:]:
        if result[-1][1] >= a and result[-1][1] < b:
            result[-1] = [result[-1][0], b]
        elif result[-1][1] >= b:
            continue
        else:
            result.append([a, b])
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
