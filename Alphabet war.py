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
    left_side = {'w' : '4', 'p' : '3', 'b' : '2', 's' : '1'}
    left = ",".join(left_side.keys())
    power_left = 0

    right_side = {'m' : '4', 'q' : '3', 'd' : '2', 'z' : '1'}
    right = ",".join(right_side.keys())
    power_right = 0

    for char in text:
        if char in left:
            power_left += int(left_side[char])
        elif char in right:
            power_right += int(right_side[char])

    if power_left > power_right:
        print("'Left side wins!'")
    elif power_left < power_right:
        print("'Right side wins!'")
    else:
        print('\"Let\'s fight again!\"')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
