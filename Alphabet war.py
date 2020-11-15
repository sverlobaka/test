def fight(text):
    """
    >>> fight('')
    "Let's fight again!"
    >>> fight('abracadabra')
    'Left side wins!'
    >>> fight('z')
    'Right side wins!'
    >>> fight('zdqmwpbs')
    "Let's fight again!"
    >>> fight('zzzzs')
    'Right side wins!'
    >>> fight('wwwwwwz')
    'Left side wins!'
    """
    side = {'w' : -4, 'p' : -3, 'b' : -2, 's' : -1, 'm' : 4, 'q' : 3, 'd' : 2, 'z' : 1}
    left_keys = ",".join(side.keys())
    power = 0

    for char in text:
        if char in left_keys or char in left_keys:
            power += side[char]

    if power < 0:
        return 'Left side wins!'
    elif power > 0:
        return 'Right side wins!'
    else:
        return "Let's fight again!"


if __name__ == '__main__':
    import doctest
    doctest.testmod()
