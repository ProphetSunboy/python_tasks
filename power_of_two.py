from math import log

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        '''
        Given an integer n, return true if it is a power of two.
        Otherwise, return false.
        '''
        if n <= 0: return False
        val = round(log(n, 2), 10)
        return val == int(val)