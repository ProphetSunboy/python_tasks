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
