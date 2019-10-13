from src.algorithm_library import *
from math import log2

def check_primality(n, cutoff, a):
    a_kfact = a
    for i in range(1, cutoff + 1):
        a_kfact = pow(a_kfact, i, n)
        b_k = (a_kfact - 1 + n) % n
        if b_k == 0:
            b_k = n

        if gcd(b_k, n) != 1 and gcd(b_k, n) != n:
            if n % b_k == 0:
                return b_k
    return 1


def prime_factorization_pollard(n, cutoff=128):
    for i in range(cutoff):
        current_p = check_primality(n, cutoff, rand_crypto(1, n))
        if current_p != 1:
            return current_p
    return 1


