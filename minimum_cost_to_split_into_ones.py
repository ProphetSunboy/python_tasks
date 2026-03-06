class Solution:
    def minCost(self, n: int) -> int:
        """
        Given an integer n, you may split an integer x into two positive integers a and b
        such that a + b = x in one operation. The cost of this operation is a * b.

        Return the minimum total cost required to split the integer n into n ones.

        Args:
            n (int): The integer to be split into n ones.

        Returns:
            int: The minimum total cost to split n into ones.

        Example:
            Input: 4
            Output: 6

        Time Complexity: O(1)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        return n * (n - 1) // 2
