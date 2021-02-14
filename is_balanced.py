def is_balanced(text):
    """
    >>> is_balanced('')
    True
    >>> is_balanced('Sensei says yes!')
    True
    >>> is_balanced('))((')
    False
    >>> is_balanced('(Sensei says yes!)')
    True
    >>> is_balanced('(Sensei says no!')
    False
    >>> is_balanced('(Sensei) (says) (yes!)')
    True
    >>> is_balanced('(Sensei (says) yes!)')
    True
    >>> is_balanced('((Sensei) says) no!)')
    False
    >>> is_balanced('(Sensei (says) (yes!))')
    True
    """
    count_open = 0
    count_close = 0

    if text.find(')') < text.find('('):
        return False
    else:
        for char in text:
            if char == '(':
                count_open += 1
            elif char == ')':
                count_close += 1

        if count_close == count_open:
            return True
        else:
            return False

if __name__ == '__main__':
    import doctest
    failures, errors = doctest.testmod()
