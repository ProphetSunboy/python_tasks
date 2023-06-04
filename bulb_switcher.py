# First method
class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
        There are n bulbs that are initially off. You first turn on all the
        bulbs, then you turn off every second bulb.
        On the third round, you toggle every third bulb (turning on if it's off
        or turning off if it's on). For the ith round, you toggle every i bulb.
        For the nth round, you only toggle the last bulb.

        Return the number of bulbs that are on after n rounds.
        """
        if n == 0:
            return 0
        i = 1
        while i ** 2 <= n:
            i += 1
        return i - 1 
    
# Second method
class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
        The floor of the square root of n gives the largest number whose square
        is less than or equal to n.
        For example, if n = 26, then the floor of square root of n is 5, which
        means the largest number whose square is less than or equal to 26 is 5
        thus for each number from 1 to 5, its respective square will be present
        in the original range. So, there are 5 perfect squares in the
        range 1 to 25 (1, 4, 9, 16, and 25).

        So, taking the floor value of the square root of n will give the number
        of perfect squares in the range 1 to n.
        """
        return int(n ** 0.5)