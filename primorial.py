from math import prod

def eratosthenes(n):
    multiples = set()
    primes = []
    for i in range(2, n+1):
        if i not in multiples:
            primes.append(i)
            for j in range(i*i, n+1, i):
                multiples.add(j)
    return primes

def num_primorial(n):
    primes = eratosthenes(10000)
    return prod(primes[:n])