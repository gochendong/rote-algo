def f(arr: list) -> list:
    """
    >>> f([2, 4, 3, 0, -1, 32, 10])
    [-1, 0, 2, 3, 4, 10, 32]
    """
    if not arr:
        return []
    base = arr[0]
    left = f([i for i in arr[1:] if i <= base])
    right = f([i for i in arr[1:] if i > base])
    return left + [base] + right


if __name__ == "__main__":
    import doctest
    doctest.testmod()
