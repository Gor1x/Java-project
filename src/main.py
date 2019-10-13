from src.parts.gen_Lukes_primes import gen_primes
from src.parts.miller_rabin_test import gen_pseudoprime
from src.parts.RSA_implementation import rsa_gen_keys
from src.parts.pollard_factorization import prime_factorization_pollard


def printing(topic):
    print('=' * len(topic))
    print(topic)
    print('=' * len(topic))


printing("Lukes primes")
print(gen_primes(), '\n')

printing("Miller-Rabin pseudo primes")
print(gen_pseudoprime(), '\n')

printing("RSA implementation")
print(rsa_gen_keys(), '\n')

printing("Pollard factorization")
print(prime_factorization_pollard(1234), '\n')
