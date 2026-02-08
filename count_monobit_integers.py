class Solution:
    def countMonobit(self, n: int) -> int:
        """
        Given an integer n, return the count of Monobit integers in the
        range [0, n] (inclusive).

        An integer is called Monobit if all bits in its binary representation
        are the same.

        Args:
            n (int): The upper bound of the range (inclusive).

        Returns:
            int: The count of Monobit integers in [0, n].

        Example:
            Input: n = 4
            Output: 3

        Time Complexity: O(log n), since we iterate over powers of two up to n.
        Space Complexity: O(1), as constant extra space is used.

        LeetCode: Beats 100% of submissions
        """
        monobit = 0
        curr_pow = 0

        while (2**curr_pow) - 1 <= n:
            monobit += 1
            curr_pow += 1

        return monobit
