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
    balanced = []
    for char in text:
        if char == '(':
            balanced.append(char)
        elif char == ')':
            if len(balanced) > 0:
                balanced.pop()
            else:
                return False

    if len(balanced) > 0:
        return False
    else:
        return True


if __name__ == '__main__':
    import doctest
    failures, errors = doctest.testmod()
