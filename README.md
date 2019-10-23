# RSA_implementation_py

Realization of concrete parts is in src/parts/, where are four .py files. 

1. [Guaranteed-prime numbers, based on Lucas primality test](https://github.com/Gor1x/RSA_implementation_py/blob/master/src/parts/gen_Lukes_primes.py)
2. [Probably-primes numbers, based on Miller-Rabin primality test](https://github.com/Gor1x/RSA_implementation_py/blob/master/src/parts/miller_rabin_test.py)
3. [Implementation of RSA Algorithm](https://github.com/Gor1x/RSA_implementation_py/blob/master/src/parts/RSA_implementation.py)
4. [Pollard's p − 1 algorithm](https://github.com/Gor1x/RSA_implementation_py/blob/master/src/parts/pollard_factorization.py)

Implementation of fast exponentiation, finding of GCD, extended Euclid Algorithm is in [algorithm implementation](https://github.com/Gor1x/RSA_implementation_py/blob/master/src/algorithm_library.py) directory

The module secrets.SystemRandom was used to generate random numbers, which are more safety.

