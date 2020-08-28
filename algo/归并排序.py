def f(arr: list) -> list:
    """
    >>> f([2, 4, 3, 0, -1, 32, 10])
    [-1, 0, 2, 3, 4, 10, 32]
    """
    mid = len(arr) >> 1
    lft, rgt = arr[:mid], arr[mid:]
    if len(lft) > 1:
        lft = f(lft)
    if len(rgt) > 1:
        rgt = f(rgt)
    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res


if __name__ == "__main__":
    import doctest
    doctest.testmod()

