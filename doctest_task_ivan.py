def compress_string(text):
    """
    >>> compress_string('dddddffeeeeg')
    'd5f2e4g'
    >>> compress_string('abcd')
    'abcd'
    """

    counter = 0
    previous = text[0]
    result = ''
    for char in text:
        if char == previous:
            counter += 1
        else:
            if counter == 1:
                result += previous
                previous = char
            else:
                result += previous + str(counter)
            counter = 1
            previous = char
    if counter != 1:
        result += previous + str(counter)
    elif counter == 1:
        result += previous
    return result


def decompress_string(text):

    """
    >>> decompress_string('a10')
    'aaaaaaaaaa'
    >>> decompress_string('a5b')
    'aaaaab'
    >>> decompress_string('a20')
    'aaaaaaaaaaaaaaaaaaaa'
    >>> decompress_string('a5sv30')
    'aaaaasvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv'
    >>> decompress_string('a20df4qs2')
    'aaaaaaaaaaaaaaaaaaaadffffqss'
    """

    symbol = []
    numeral = ''
    result = ''
    counter = 0
    for char in text:
        if char >= '0' and char <= '9':
            numeral += char
            counter += 1
        else:
            if counter >= 1:
                result += symbol * (int(numeral) - 1)
                counter = 0
            symbol = char
            result += symbol
            numeral = ''

    if numeral >= '0' and numeral <= '9':
        result += symbol * (int(numeral) - 1)
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
