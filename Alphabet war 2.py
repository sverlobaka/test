def fight(text):
    """
    >>> fight('')
    "Let's fight again!"
    >>> fight('abracadabra')
    'army3 wins!'
    >>> fight('wmu')
    "Let's fight again!"
    """

    army = {
        'army1': {'w': 4, 'p': 3, 'b': 2, 's': 1},
        'army2': {'m': 4, 'q': 3, 'd': 2, 'z': 1},
        'army3': {'a': 4, 'e': 3, 'o': 2, 'u': 1, 'i': 1}
    }
    power = {}

    for name_army in army:
        power[name_army] = 0
        for char in text:
            power[name_army] += army[name_army].get(char, 0)
    max_power = max(power.values())
    max_power_army = list(power.keys())[list(power.values()).index(max_power)]
    count_max_power = 0
    for key in power.keys():
        if power[key] == max_power:
            count_max_power += 1
    if count_max_power > 1:
        return 'Let\'s fight again!'
    else:
        return f"{max_power_army} wins!"


if __name__ == '__main__':
    import doctest
    doctest.testmod()
