from src.parts.miller_rabin_test import gen_pseudoprime
from src.algorithm_library import *


def get_opposite(e, phi):
    x, y = gcd_extended(e, phi)
    if x < 0:
        x += phi
    return x


def rsa_gen_keys():
    """Генерация открытого и секретного ключей.

    Возвращает кортеж (n, p, q, e, d), где
    n = p*q;
    p, q — сильно псевдопростые по не менее чем log(q) основаниям;
    e — целое число, меньшее n и взаимно простое с phi(n), значением функции Эйлера от n,
    d — целое число, обратное к e по модулю phi(n)."""
    p = gen_pseudoprime()
    q = gen_pseudoprime()
    phi = (p - 1) * (q - 1)
    e = gen_pseudoprime()
    d = get_opposite(e, phi)
    return (p * q, p, q, e, d)


def rsa_encrypt(n, e, t):
    """Шифрование по RSA.

    На входе открытый ключ n, e и сообщение t.
    Возвращает целое число, равное t^e mod n."""
    return pow(t, e, n)


def rsa_decrypt(n, d, s):
    """Дешифрование по RSA.

    На входе закрытый ключ n, d и зашифрованное сообщение s.
    Возвращает целое число, равное s^d mod n."""
    return pow(s, d, n)
