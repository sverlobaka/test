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
    result = []
    intervals.sort()
    for a, b in intervals:
        if len(result) == 0:
            result.append([a, b])
        else:
            if result[-1:][0][1] >= a and result[-1:][0][1] < b:
                result[-1:] = [[result[-1:][0][0], b]]
            elif result[-1:][0][1] >= b:
                pass
            else:
                result.append([a, b])
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
