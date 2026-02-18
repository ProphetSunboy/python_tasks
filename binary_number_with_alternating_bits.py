# First Solution
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        """
        Given a positive integer, check whether it has alternating bits: namely,
        if two adjacent bits will always have different values.

        :param int n: positive integer
        :returns alterating_bits: two adjacent bits of binary representation of
        n will always have different values

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 91.57%
        """
        b = bin(n)[2:]

        for i in range(1, len(b)):
            if b[i] == b[i - 1]:
                return False

        return True


# Second Solution
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        """
        Check whether a positive integer has alternating bits.

        Two adjacent bits must always have different values.

        Args:
            n (int): Input positive integer.

        Returns:
            bool: True if the binary representation of n has alternating bits,
                False otherwise.

        Example:
            Input: n = 5
            Output: true

        Time Complexity: O(log n) - Iterates through the bits of n.
        Space Complexity: O(1) - Uses constant extra space.

        LeetCode: Beats 100% of submissions
        """
        prev = n & 1
        n //= 2

        while n > 0:
            if n & 1 == prev:
                return False

            prev = n & 1
            n //= 2

        return True
