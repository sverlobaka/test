def sort_letters(text):
    """
    >>> sort_letters('aaabccccdeefffff')
    'fffffccccaaaeebd'
    >>> sort_letters('abcdefghijklmnop')
    'abcdefghijklmnop'
    >>> sort_letters('')
    ''
    >>> sort_letters('aba')
    'aab'
    >>> sort_letters('abcabccba')
    'aaabbbccc'
    >>> sort_letters('dcbeeaaabccbadeee')
    'eeeeeaaaacccbbbdd'
    """

    frequency_by_letter = {}
    for char in text:
        if char not in frequency_by_letter:
            frequency_by_letter[char] = 1
        else:
            frequency_by_letter[char] += 1

    index_by_letter = {}
    for i, char in enumerate(text):
        if char not in index_by_letter:
            index_by_letter[char] = i

    triplets = []
    for key, value in frequency_by_letter.items():
        x = [value, -index_by_letter[key], key]
        triplets.append(x)

    sorted_triplets = sorted(triplets, reverse=True)  # O(k * logK(k))
    # print(sorted_triplets)
    result = [
        char * f
        for f, _, char in sorted_triplets
    ]
    # result = []
    # for f, _, char in sorted_triplets:
    #     result.append(char * f)
    return ''.join(result)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
