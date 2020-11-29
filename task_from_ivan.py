def fight(text):
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
    max_power = max(power.values())
    max_power_army = list(power.keys())[list(power.values()).index(max_power)]

    return max_power_army
