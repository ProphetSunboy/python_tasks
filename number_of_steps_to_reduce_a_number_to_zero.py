class Solution:
    def numberOfSteps(self, num: int) -> int:
        """
        Given an integer num, return the number of steps to reduce it to zero.

        In one step, if the current number is even, you have to divide it by 2,
        otherwise, you have to subtract 1 from it.


        LeetCode Beats 100%
        """
        steps = 0

        while num > 0:
            if num % 2:
                num -= 1
            else:
                num //= 2

            steps += 1

        return steps
