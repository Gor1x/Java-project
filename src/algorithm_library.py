from secrets import *

PSEUDO_SIMPLE_MIN = 2 ** 123
PSEUDO_SIMPLE_MAX = 2 ** 128

randomizer = SystemRandom()


def rand_crypto(a, b):
    return SystemRandom.randrange(randomizer, a, b)


def is_simple(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def get_list_of_primes(n):
    list_simples = []
    for i in range(2, n + 1):
        if is_simple(i):
            list_simples.append(i)
    return list_simples


def fast_pow(elem, b, mod):
    if b == 0:
        return 1
    sqr = fast_pow(elem, b // 2, mod)
    sqr = sqr * sqr
    if b % 2 == 1:
        sqr = sqr * elem
    return sqr % mod


def gcd_extended(a, b, x1=1, y1=0, x2=0, y2=1):
    if a == 0:
        return x2, y2
    elif b == 0:
        return x1, y1

    if a > b:
        k = a // b
        a = a % b
        x1 = x1 - k * x2
        y1 = y1 - k * y2
    else:
        k = b // a
        b = b % a
        x2 = x2 - k * x1
        y2 = y2 - k * y1
    return gcd_extended(a, b, x1, y1, x2, y2)


def gcd(a, b):
    while b:
        a %= b
        b, a = a, b
    return a
