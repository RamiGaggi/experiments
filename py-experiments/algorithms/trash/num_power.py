# Num to any power.

def my_power(a, n):
    """My recursion solution"""
    def inner_power(num, power):
        if power == 0:
            return 1
        return inner_power(num, power - 1) * num

    if n >= 0:
        return inner_power(a, n)
    else:
        return 1 / inner_power(a, abs(n))


def power(a, n):
    """Reference solution"""
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res
