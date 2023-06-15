from math import factorial as fact

class Solution:
    def is_prime(self, num):
        """
        Return True if num is prime, False otherwise.
        """
        if num == 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def numPrimeArrangements(self, n: int) -> int:
        """
        Return the number of permutations of 1 to n so that prime numbers are
        at prime indices (1-indexed.)

        Since the answer may be large, return the answer modulo 10^9 + 7.
        """
        n_primes = 0
        for i in range(1, n+1):
            if self.is_prime(i):
                n_primes += 1

        return fact(n - n_primes) * fact(n_primes) % (10 ** 9 + 7)