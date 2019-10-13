from math import log2
from src.algorithm_library import *


def build_pseudo_prime(list_of_simples):
    number = 2
    taken_simples = {2}
    while number < PSEUDO_SIMPLE_MIN:
        pos = rand_crypto(0, len(list_of_simples) - 1)

        for i in (1, rand_crypto(1, 4)):
            if number * list_of_simples[pos] > PSEUDO_SIMPLE_MAX:
                continue
            taken_simples.add(list_of_simples[pos])
            number = number * list_of_simples[pos]
            if number * list_of_simples[pos] > PSEUDO_SIMPLE_MAX:
                continue
            number = number * list_of_simples[pos]

    if len(taken_simples) < 5:
        return build_pseudo_prime(list_of_simples)
        # works if current is incorrect

    return number + 1, taken_simples


def test_a(a, n, taken_primes):
    for p in taken_primes:
        if fast_pow(a, (n - 1) // p, n) == 1:
            return False
    return True


def check_primality(n, taken_primes):
    tester = 2
    max_a = int(log2(n) + 1)
    while tester <= max_a:
        if fast_pow(tester, n - 1, n) == 1 and test_a(tester, n, taken_primes):
            return tester
        tester += 1
    return -1


def gen_primes():
    """Генерация доказуемо простых на основе теста Люка.

    Возвращает кортеж (n, ps, a), где
    n — простое между 2^123 и 2^128;
    ps — список простых, на которые раскладывается n-1;
    a — число, удовлетворяющее тесту Люка."""

    primes = get_list_of_primes(128)

    while True:  # till answer is not found

        n, taken = build_pseudo_prime(primes)

        answer = check_primality(n, taken)

        if answer != -1:  # in case of errors
            return (n, primes, answer)

