import sys
from math import *
sys.setrecursionlimit(1000000)
def f(n):
    if n <= 100:
        return pi**n
    else:
        if n % 2 ==0:
            return f(n-1) + (n ** 2)
        else:
            return 2 * f(n-2)
        
print(f(298) - 2 * f(295))