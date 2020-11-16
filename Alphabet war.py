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

    side = {
        'y': {'left': -1, 'right': 3},
        'w': {'left': -4, 'right': 0},
        'p': {'left': -3, 'right': 0},
        'b': {'left': -2, 'right': 0},
        's': {'left': -1, 'right': 0},
        'm': {'left': 0, 'right': 4},
        'q': {'left': 0, 'right': 3},
        'd': {'left': 0, 'right': 2},
        'z': {'left': 0, 'right': 1}
    }
    keys = ",".join(side.keys())
    power = 0

    for char in text:
        if char in keys:
            power += side[char]['left'] + side[char]['right']

    if power < 0:
        return 'Left side wins!'
    elif power > 0:
        return 'Right side wins!'
    else:
        return "Let's fight again!"


if __name__ == '__main__':
    import doctest
    doctest.testmod()
