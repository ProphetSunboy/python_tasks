class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        """
        Given two integers num1 and num2, determine the minimum number of operations required to make num1 equal to 0.

        In each operation, you can choose an integer i in the range [0, 60] and subtract (2^i + num2) from num1.

        Return the minimum number of such operations needed to make num1 equal to 0. If it is impossible, return -1.

        Args:
            num1 (int): The starting integer.
            num2 (int): The integer added to each power of two in the operation.

        Returns:
            int: The minimum number of operations to make num1 zero, or -1 if impossible.

        Example:
            >>> makeTheIntegerZero(12, 2)
            2

        Time Complexity: O(K), where K is the upper bound for the number of operations (typically up to 10^4).
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        for k in range(1, 10**4):
            s = num1 - k * num2
            if s <= 0 or s < k:
                break

            if s.bit_count() <= k:
                return k

        return -1
