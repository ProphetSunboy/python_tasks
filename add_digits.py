class Solution:
    def addDigits(self, num: int) -> int:
        '''
        Given an integer num, repeatedly adds all its digits
        until the result has only one digit, and returns it.
        '''
        return 1 + (num - 1) % 9 if num else 0