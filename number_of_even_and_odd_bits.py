class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        """
        Given a positive integer n, count the number of 1-bits at even and odd indices in its binary representation.

        Bits are indexed from right to left (least significant bit is index 0).

        Returns:
            list[int]: [even, odd], where
                - even is the number of 1-bits at even indices,
                - odd is the number of 1-bits at odd indices.

        Example:
            >>> evenOddBit(17)  # binary: 10001
            [2, 0]
            >>> Solution().evenOddBit(2)   # binary: 10
            [0, 1]

        Time complexity: O(log n)
        Space complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        bin_n = bin(n)[2:][::-1]
        bits = [0, 0]

        for i, bit in enumerate(bin_n):
            if bit == "1":
                bits[i % 2] += 1

        return bits
