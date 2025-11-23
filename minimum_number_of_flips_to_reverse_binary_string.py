class Solution:
    def minimumFlips(self, n: int) -> int:
        """
        Given a positive integer n, return the minimum number of flips required
        to make s equal to the reverse of its original form.

        Each bit flip in s changes a 0 to 1 or a 1 to 0.
        The binary representation does not include leading zeros.

        Args:
            n (int): The integer to process.

        Returns:
            int: The minimum number of flips required to make s equal to the
            reverse of its original form.

        Example:
            Input: n = 27  # binary '11011'
            Output: 0

            Input: n = 10  # binary '1010'
            Output: 4

        Time Complexity: O(k), where k is the number of bits in n.
        Space Complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        bin_n = bin(n)[2:]

        i, j = 0, len(bin_n) - 1
        flips = 0
        while i < len(bin_n):
            if bin_n[i] != bin_n[j]:
                flips += 1
            i += 1
            j -= 1

        return flips
