# miller(d, n) function uses randint for once. I didn't use my randomZ to reduce errors.
import random


def modex(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res


def miller(d, n):
    a = 2 + random.randint(1, n - 4)
    x = modex(a, d, n)

    if x == 1 or x == n - 1:
        return True

    while d != n - 1:
        x = (x * x) % n
        d *= 2

        if x == 1:
            return False
        if x == n - 1:
            return True
    return False


# 40 rounds of miller(k=40) is the most efficient amount of rounds while safe
def prime_check(n, k=40):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    d = n - 1
    while d % 2 == 0:
        d //= 2

    for i in range(k):
        if not miller(d, n):
            return False
    return True

# To use miller: import miller, then use miller.prime_check(n)
# Note that prime_check(n) returns booleans
