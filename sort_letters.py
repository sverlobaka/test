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
    sorted_text = {}
    result = ''
    for char in text:
        if text_counter.get(char):
            text_counter[char] += 1
        else:
            text_counter[char] = 1
    sorted_keys = sorted(text_counter, key=text_counter.get, reverse=True)

    for keys in sorted_keys:
        sorted_text[keys] = text_counter[keys]

    for keys in sorted_text:
        result += keys * sorted_text[keys]
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
