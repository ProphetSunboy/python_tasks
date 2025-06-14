class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        """Finds the smallest positive integer that is a multiple of both 2 and n.

        Given a positive integer n, returns the smallest number that is divisible by both 2 and n.

        Args:
            n (int): A positive integer

        Returns:
            int: The smallest positive integer that is a multiple of both 2 and n

        Examples:
            >>> smallestEvenMultiple(5)
            10  # 10 is the smallest number divisible by both 2 and 5
            >>> smallestEvenMultiple(6)
            6   # 6 is already divisible by both 2 and 6

        Time complexity: O(1) - constant time operation
        Space complexity: O(1) - no extra space needed

        LeetCode: Beats 100% of submissions
        """
        return n if n % 2 == 0 else n * 2
