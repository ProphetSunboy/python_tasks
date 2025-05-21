class Solution:
    def numberOfSteps(self, num: int) -> int:  # Time: O(log n)
        """
        Given an integer num, return the number of steps to reduce it to zero.

        In one step, if the current number is even, you have to divide it by 2,
        otherwise, you have to subtract 1 from it.

        :param int num: integer number to reduce to zero
        :returns int: number of steps needed to reduce num to zero

        Time complexity: O(log n)
        Space complexity: O(1)

        LeetCode: Beats 100%
        """
        steps = 0

        while num > 0:
            if num % 2:
                num -= 1
            else:
                num //= 2

            steps += 1

        return steps
