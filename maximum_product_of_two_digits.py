class Solution:
    def maxProduct(self, n: int) -> int:
        """
        Given a positive integer n, return the maximum product of any two digits in n.

        You may use the same digit twice if it appears more than once in n.

        Args:
            n (int): The positive integer whose digits will be considered.

        Returns:
            int: The maximum product of any two digits in n.

        Examples:
            >>> maxProduct(1234)
            12
            >>> maxProduct(505)
            25

        Time Complexity: O(d), where d is the number of digits in n.
        Space Complexity: O(d)

        LeetCode: Beats 100% of submissions
        """
        sorted_digits = sorted(str(n))

        return int(sorted_digits[-1]) * int(sorted_digits[-2])
