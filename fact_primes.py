def prime(N):
    primes = []
    while N > 1:
        div, count = 2, 0
        while div <= N / 2 and count == 0:
            if N % div == 0:
                   count += 1
            div += 1
        if count == 0:
            primes.append(N)
        N -= 1
    return primes

N = 5
primes = prime(N)[::-1]
powers = [sum(N // num ** i for i in range(1,21+1) if num ** i <= N) for num in primes]
print(' * '.join([str(primes[i]) + '^' + str(powers[i]) if powers[i] > 1 else str(primes[i]) for i in range(len(primes))]))