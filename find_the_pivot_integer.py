class Solution:
    def pivotInteger(self, n: int) -> int:
        """Finds the pivot integer for a given positive integer n.

        The pivot integer `x` is the integer where the sum of all elements
        between 1 and `x` (inclusive) equals the sum of all elements between
        `x` and `n` (inclusive).

        Args:
            n (int): A positive integer.

        Returns:
            int: The pivot integer `x` if it exists, otherwise -1.

        Example:
            Input: n = 8
            Output: 6
            Explanation: The sum of the numbers from 1 to 6 is 21.
                         The sum of the numbers from 6 to 8 is 21.

        Time complexity: O(n), where n is the input integer.
        Space complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        pivot = n
        left_sum = (n * (n + 1)) // 2
        right_sum = n

        while left_sum > right_sum:
            pivot -= 1
            left_sum -= pivot + 1
            right_sum += pivot

        return pivot if left_sum == right_sum else -1
