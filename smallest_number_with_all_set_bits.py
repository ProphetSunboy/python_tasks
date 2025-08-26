class Solution:
    def smallestNumber(self, n: int) -> int:
        """
        Given a positive integer n, return the smallest integer x such that:
            - x >= n
            - The binary representation of x contains only set bits (i.e., all bits are 1).

        Args:
            n (int): The input positive integer.

        Returns:
            int: The smallest number >= n with all bits set in its binary representation.

        Example:
            >>> smallestNumber(6)
            7
            >>> smallestNumber(15)
            15

        Time Complexity: O(log n)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        curr = 1

        while curr < n:
            curr = curr * 2 + 1

        return curr
