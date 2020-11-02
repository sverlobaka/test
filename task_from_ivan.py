def compress_string (text):
    counter = 0
    previous = text[0]
    compress = ''
    for element in text:
        if element == previous:
            counter = counter + 1
            previous = element
        else:
            if counter == 1:
                compress = str(compress) + str(previous)
                counter = 1
                previous = element
            elif counter == 0:
                compress = compress
            else:
                compress = str(compress) + str(previous) + str(counter)
            counter = 1
            previous = element
    compress = str(compress) + str(previous) + str(counter)
    return compress

def decompress_string(text):
    symbol = text[0]
    numeral = '0'
    decompress = ''
    for element in text:
        if element >= '0' and element <= '9':
            numeral = str(numeral) + str(element)
            decompress = decompress + symbol * (int(numeral) - 1)
        else:
            symbol = element
            decompress = decompress + symbol
            numeral = ''
    return decompress



