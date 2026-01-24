def fact(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s

def f(n):
    if n >= 1000:
        return fact(n)
    else:
        if n % 2 ==0:
            return f(n+1) * (n//2)
        else:
            return f(n + 2) *n
        
print(f(18) / f(20))