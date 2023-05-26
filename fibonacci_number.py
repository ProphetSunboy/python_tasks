class Solution:
    def fib(self, n: int) -> int:
        """
        The Fibonacci numbers, commonly denoted F(n) form a sequence,
        called the Fibonacci sequence, such that each number is
        the sum of the two preceding ones, starting from 0 and 1.
        Given n calculate F(n).
        (this solution is about 20 times faster than recurrence)
        """
        if n == 0:
            return 0
        v = 0
        m = 1
        for _ in range(n-1):
            m, v = m + v, m
        return m