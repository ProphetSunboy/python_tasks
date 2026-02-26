class Solution:
    def numSteps(self, s: str) -> int:
        """
        Given a binary representation of an integer as a string `s`, return the
        number of steps to reduce it to 1 under the following rules:

        - If the current number is even, divide it by 2.
        - If the current number is odd, add 1 to it.

        It is guaranteed that you can always reach 1 for all test cases.

        Args:
            s (str): Binary representation of an integer.

        Returns:
            int: The number of steps required to reduce the number to 1.

        Example:
            Input: s = "1101"
            Output: 6

        Time Complexity: O(log n), where n is the integer value of s.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        num = int(s, 2)
        steps = 0

        while num > 1:
            if num % 2 == 0:
                num >>= 1
            else:
                num += 1

            steps += 1

        return steps
