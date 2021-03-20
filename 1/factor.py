from random import randint
from math import gcd, pi
from functools import reduce
from datetime import datetime

#Ро-алгоритм Полларда
def f(x, a, b):
    return a * x ** 2 + b

def is_prime(N):
    if N in (0, 1):
        return False
    if N == 2:
        return True
    if N % 2 == 0:
        return False
    s = N - 1
    while s % 2 == 0:
        s //= 2
    for i in range(50):
        a = randint(1, N - 1)
        exp = s
        mod = pow(a, exp, N)
        while exp != N - 1 and mod != 1 and mod != N - 1:
            mod = mod * mod % N
            exp *= 2
        if mod != N - 1 and exp % 2 == 0:
            return False
    return True

def find_factor(n):
    maxiterssq = pi / 4 * n
    x = randint(1, n - 1)
    y = x
    d = 1
    iters = 0
    a = randint(1, n - 1)
    b = randint(1, n - 1)
    while d in (1, n):
        if iters ** 2 > maxiterssq:
            a = randint(1, n - 1)
            b = randint(1, n - 1)
            x = randint(1, n - 1)
            y = x
            iters = 0
        x = f(x, a, b) % n
        y = f(f(y, a, b), a, b) % n
        d = gcd(abs(x - y), n)
        iters += 1
    return d


def find_prime_factor(n, factors):
    if is_prime(n):
        factors.append(n)
    else:
        tmp = n // find_factor(n)
        find_prime_factor(tmp, factors)


def factor(n, factors):
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n % 3 == 0:
        factors.append(3)
        n //= 3
    while n > 1:
        find_prime_factor(n, factors)
        n //= factors[-1]


def find_all_factors(prime_factors, all_factors):
    all_factors.append(1)
    all_factors.append(prime_factors[0])
    for i in range(1, len(prime_factors)):
        tmp = []
        for f in all_factors:
            if f * prime_factors[i] not in all_factors:
                tmp.append(f * prime_factors[i])
        all_factors += tmp
    all_factors.sort()


def pollard_rho(n):
    factors = []
    factor(n, factors)
    factors.sort()
    all_factors = []
    find_all_factors(factors, all_factors)
    return all_factors
    
n = 1197606395839410537256528037313284196976497391762438410219156212428076186085911
print('Первое число',n)
factors = pollard_rho(n)
factors = factors[1:len(factors) - 2]
print('Простые делители',*factors,sep='\n')
