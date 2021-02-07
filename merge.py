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

    for char in range(len(intervals)):
        intervals[char].sort()
    intervals.sort()

    for char in intervals:
        if len(result) == 0:
            result.append(char)
        else:
            if result[(len(result) - 1)][1] >= char[0] and result[(len(result) - 1)][1] < char[1]:
                result[(len(result) - 1)] = [result[(len(result) - 1)][0], char[1]]
            elif result[(len(result) - 1)][1] and result[(len(result) - 1)][1] >= char[1]:
                result[(len(result) - 1)] = result[(len(result) - 1)]
            else:
                result.append(char)
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
