class Solution:
    def divide_by_three(self, n):
        while n % 3 == 0:
            n //= 3
        return n

    def isPowerOfThree(self, n: int) -> bool:
        '''
        Given an integer n, return true if it is a power of three.
        Otherwise, return false.
        '''
        if n <= 0:
            return False
        return self.divide_by_three(n) == 1