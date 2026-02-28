class Solution:
    def concatenatedBinary(self, n: int) -> int:
        """
        Returns the decimal value of the binary string formed by concatenating
        the binary representations of numbers from 1 to n in sequence,
        modulo 10^9 + 7.

        Args:
            n (int): Inclusive upper bound of the range.

        Returns:
            int: Decimal value of the concatenated binary numbers modulo 10^9 + 7.

        Example:
            Input: n = 3
            Output: 27

        Time Complexity: O(n).
        Space Complexity: O(1).
        """
        MOD = 10**9 + 7
        curr_num = 0
        bit_length = 0

        for num in range(1, n + 1):
            if num & (num - 1) == 0:
                bit_length += 1

            curr_num = ((curr_num << bit_length) | num) % MOD

        return curr_num
