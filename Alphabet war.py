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

    for name_army in army.keys():
        power[name_army] = 0
        for char in text:
            if army[name_army].get(char):
                power[name_army] += army[name_army].get(char)
    max_power_befor = max(power.values())
    max_power_army_befor = list(power.keys())[list(power.values()).index(max_power_befor)]
    power_compare = {}
    power_compare[max_power_army_befor] = max_power_befor
    del power[max_power_army_befor]
    max_power_after = max(power.values())
    max_power_army_after = list(power.keys())[list(power.values()).index(max_power_after)]
    power_compare[max_power_army_after] = max_power_after

    if power_compare[max_power_army_befor] != power_compare[max_power_army_after]:
        return "" + max_power_army_befor + " wins!"
    else:
        return "Let's fight again!"

if __name__ == '__main__':
    import doctest
    doctest.testmod()
