from functools import lru_cache

@lru_cache(None)
def f(x):
    if x == 150:
        return 1
    if x > 150:
        return 0

    ans = f(x + 1)  # команда A

    s = str(x)
    if int(s[1]) < int(s[2]):  # команда B разрешена
        y = int(s[0] + s[2] + s[1])
        ans += f(y)

    return ans

print(f(100))