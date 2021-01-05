# 斐波那契数列的三种解法(值得反复思考的经典)
# 也是分解问题的三种方法, 思考优先级依次递减

# 1.直接遍历(使用滚动变量)


def f(n: int) -> int:
    """
    >>> f(10)
    55
    """
    a, b = 0, 1
    for i in range(n):
        # tmp = a
        # a = a + b
        # b = tmp
        a, b = b, a + b  # 很多语言不支持这种写法
    return a


# 2.动态规划(用数组记录子问题的解)


def f2(n: int) -> int:
    """
    >>> f2(10)
    55
    """
    if n == 0:
        return 0  # 避免dp[1] = 1出错
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1]


# 3.递归(常用于复杂的搜索算法)


def f3(n: int) -> int:
    """
    >>> f3(10)
    55
    """
    if n <= 1:
        return n  # 递归必然有一个终止的return
    return f3(n - 1) + f3(n - 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
