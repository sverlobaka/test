def is_balanced(text):
    """
    >>> is_balanced("")
    True
    >>> is_balanced("Sensei says yes!")
    True
    >>> is_balanced("))((")
    False
    >>> is_balanced("(Sensei says yes!)")
    True
    >>> is_balanced("(Sensei says no!")
    False
    >>> is_balanced("(Sensei) (says) (yes!)")
    True
    >>> is_balanced("(Sensei (says) yes!)")
    True
    >>> is_balanced("((Sensei) says) no!)")
    False
    >>> is_balanced("(Sensei (says) (yes!))")
    True
    >>> is_balanced("(Sensei [says] yes!)")
    True
    >>> is_balanced("(Sensei [says) no!]")
    False
    """

    balanced = []
    open_close = {"(": ")", "[": "]", "{": "}"}
    count_quote = 0
    for char in text:
        if char in open_close:
            balanced.append(char)
        elif char in open_close.values():
            if len(balanced) > 0 and char in open_close[balanced[-1]]:
                balanced.pop()
            else:
                return False
    return  not bool(balanced)

if __name__ == '__main__':
    import doctest
    failures, errors = doctest.testmod()
