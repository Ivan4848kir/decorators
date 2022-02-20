import math
def cash(func):
    _cash={}
    def wrapped(*args, **kwargs):
        nonlocal _cash
        if not _cash.get(args):
            res=func(*args, **kwargs)
            _cash[args]=res
            return func(*args, **kwargs)
        else:
            return _cash[args]
    return wrapped

@cash
def factorial(n):
    factorial = 1
    for i in range(1, n):
        factorial *= i
    return factorial


print(factorial(10))



