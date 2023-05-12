class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        Given a non-negative integer x, returns the square
        root of x rounded down to the nearest integer. 
        '''
        if x < 2:
            return x
        low, high = 1, x
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                low = mid + 1
            else:
                high = mid - 1
        return high