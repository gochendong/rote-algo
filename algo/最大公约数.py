def f(a, b: int) -> int:
    """
    >>> f(25, 10)
    5
    >>> f(11, 40)
    1
    """
    if a % b == 0:
        return b
    else:
        return f(b, a % b)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
