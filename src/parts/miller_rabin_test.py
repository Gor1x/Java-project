from math import log2
from src.algorithm_library import *


def miller_rabin_test(a, n, d):
    if pow(a, n - 1, n) != 1:
        return False

    current = pow(a, d, n)
    flag_minus_one = False
    while current != 1:
        if current == n - 1:
            flag_minus_one = True
        current = ((current * current) % n + n) % n

    return flag_minus_one


def erase_twos_from(n):
    while (n & 1) == 0:
        n = n >> 1
    return n


def check_primality_miller_rabin(n, list_of_primes):
    for prime in list_of_primes:
        if n % prime == 0:
            return False

    log_n = int(log2(n) + 1)

    d = erase_twos_from(n - 1)
    for i in range(log_n):
        a = rand_crypto(log_n, n)
        if not miller_rabin_test(a, n, d):
            return False
    return True


def gen_pseudoprime():
    """Генерация псевдопростых на основе теста Миллера—Рабина.

    Возвращает целое число n в диапазоне от 2^123 до 2^128,
    псевдопростое по основание не менее чем log(n) чисел."""
    list_of_primes = get_list_of_primes(400)
    while True:
        n = rand_crypto(PSEUDO_SIMPLE_MIN, PSEUDO_SIMPLE_MAX)
        if check_primality_miller_rabin(n, list_of_primes):
            return n
