class Solution:
    def isPerfectSquare(self, num: int) -> bool: 
        '''
        Given a positive integer num, return true if num
        is a perfect square or false otherwise.
        ''' 
        sqrt_num = num // 2  
        while sqrt_num * sqrt_num > num:  
            sqrt_num = (sqrt_num + num // sqrt_num) // 2  
        return sqrt_num * sqrt_num == num or num == 1