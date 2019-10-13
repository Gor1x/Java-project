# RSA_implementation_py
python: Implementation of RSA algorithm

Реализации конкретных частей находятся в src/parts/, там находятся четыре .py файла с реализацией конкретных заданий, исключая возведение в степень по модулю. 


1. [Доказуемо простые числа](https://github.com/Gor1x/RSA_implementation_py/blob/master/src/parts/gen_Lukes_primes.py)
2. [Тест Миллера-Рабина, вероятно простые числа](https://github.com/Gor1x/RSA_implementation_py/blob/master/src/parts/miller_rabin_test.py)
3. [Реализация алгоритма RSA](https://github.com/Gor1x/RSA_implementation_py/blob/master/src/parts/RSA_implementation.py)
4. [p - 1 метод факторизации Полларда](https://github.com/Gor1x/RSA_implementation_py/blob/master/src/parts/pollard_factorization.py)

Реализация быстрого возведения в степень, поиска наибольшего общего делителя, расширенного алгоритма Евклида находится в файле [реализации алгоритмов](https://github.com/Gor1x/RSA_implementation_py/blob/master/src/algorithm_library.py)

Для получения рандомных чисел был использован модуль secrets.SystemRandom.

Также в реализации теста Миллера-Рабина я посчитал, что будет неплохим дополнением проверять делится ли число на простые числа до 400.
