import sys
sys.setrecursionlimit(10*5)
def f(n):
    return g(n-1) - g(n-5)


def g(n):
    if n <= 25:
        return 2 * (n + 1)
    else:
        return g(n-2) +n
    
f(150774)