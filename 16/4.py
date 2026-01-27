from functools import *
import sys
sys.setrecursionlimit(10000)
@lru_cache()
def f(n):
    return 2 * (g(n-3)+8)
@lru_cache()
def g(n):
    if n < 10:
        return 2 * n
    return g(n-2) + 1

print(f(15548))