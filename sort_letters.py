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

    text_counter = {}
    sorted_text = []
    result = ''
    for char in text:
        if text_counter.get(char):
            continue
        else:
            text_counter[char] = text.count(char)

    for keys, values in text_counter.items():
        x = [values, keys]
        sorted_text.append(x)
    sorted_text = sorted(sorted_text, reverse=True)
    for i in range(len(sorted_text)):
        result += sorted_text[i][0] * sorted_text[i][1]
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
