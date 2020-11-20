def fight(text):
    """
    >>> fight('')
    "Let's fight again!"
    >>> fight('abracadabra')
    'Headless side wins!'
    >>> fight('z')
    'Right side wins!'
    >>> fight('zdqmwpbs')
    "Let's fight again!"
    >>> fight('zzzzs')
    'Right side wins!'
    >>> fight('wwwwwwz')
    'Left side wins!'
    >>> fight('wpbs')
    'Left side wins!'
    >>> fight('aeub')
    'Headless side wins!'

    """

    side = {
        'w': {'left': 4, 'right': 0, 'headless': 0},
        'p': {'left': 3, 'right': 0, 'headless': 0},
        'b': {'left': 2, 'right': 0, 'headless': 0},
        's': {'left': 1, 'right': 0, 'headless': 0},
        'm': {'left': 0, 'right': 4, 'headless': 0},
        'q': {'left': 0, 'right': 3, 'headless': 0},
        'd': {'left': 0, 'right': 2, 'headless': 0},
        'z': {'left': 0, 'right': 1, 'headless': 0},
        'a': {'left': 0, 'right': 0, 'headless': 1},
        'e': {'left': 0, 'right': 0, 'headless': 1},
        'o': {'left': 0, 'right': 0, 'headless': 1},
        'u': {'left': 0, 'right': 0, 'headless': 1},
    }
    power_left = 0
    power_right = 0
    power_headless = 0

    for char in text:
        if side.get(char):
            power_left += side[char]['left']
            power_right += side[char]['right']
            power_headless += side[char]['headless']

    if power_left > power_right and power_left > power_headless:
        return 'Left side wins!'
    elif power_right > power_left and power_right > power_headless:
        return 'Right side wins!'
    elif power_headless > power_left and power_headless > power_right:
        return "Headless side wins!"
    else:
        return "Let's fight again!"


if __name__ == '__main__':
    import doctest
    doctest.testmod()
