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
    open = ["(", "[", "{"]
    close = [")", "]", "}"]
    count_quote = 0
    for char in text:
        if char in open:
            balanced.append(char)
        elif char in close:
            if len(balanced) > 0 and open.index(balanced[-1]) == close.index(char):
                balanced.pop()
            else:
                return False

    if balanced:
        return False
    else:
        return True

if __name__ == '__main__':
    import doctest
    failures, errors = doctest.testmod()
