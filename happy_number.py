class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        Determines if a number n is happy.
        A happy number is a number defined by the following process:
            Starting with any positive integer, replace
                the number by the sum of the squares of its digits.
            Repeat the process until the number equals 1
                (where it will stay), or it loops endlessly
                in a cycle which does not include 1.
            Those numbers for which this process ends in 1 are happy.
        Returns True if n is a happy number, and False if not.
        '''
        seen = set()
        while True:
            n = sum(int(num) ** 2 for num in str(n))
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)