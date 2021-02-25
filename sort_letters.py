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
    """

    if len(text) < 1:
        return text
    else:
        text_sort = sorted(text)
        counters = [''] * len(text_sort)
        result = ''
        j = text_sort[0]
        for i in text_sort:
            if j == i:
                continue
            else:
                x = text_sort.count(j)
                counters[x] += j
                j = i
                count = 1
        x = text_sort.count(i)
        counters[x] += i

        for i in range((len(counters) - 1), -1, -1):
            if counters[i] != '':
                for char in counters[i]:
                    char = char * i
                    result += char
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
