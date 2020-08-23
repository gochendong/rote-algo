def f(n: int) -> dict:
    """
    >>> f(5**8 * 23**5 * 43**9)
    defaultdict(<class 'int'>, {5: 8, 23: 5, 43: 9})
    """
    from _collections import defaultdict
    m = defaultdict(int)
    while n > 1:
        for i in range(2, n+1):
            if n % i == 0:
                n = n // i
                m[i] += 1
                break
    return m


if __name__ == "__main__":
    import doctest
    doctest.testmod()
