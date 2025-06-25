class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        """Rearranges the bits of a binary string to form the maximum odd binary number.

        Given a binary string `s` containing at least one '1', this function rearranges
        its bits to create the largest possible odd binary number (i.e., a binary number
        ending with '1') that can be formed from the same combination of bits.

        The resulting string may have leading zeros.

        Args:
            s (str): The input binary string containing at least one '1'.

        Returns:
            str: The maximum odd binary number as a string.

        Example:
            >>> maximumOddBinaryNumber("010")
            '001'
            >>> maximumOddBinaryNumber("0101")
            '1001'

        LeetCode: Beats 100% of submissions
        """
        c = Counter(s)

        max_odd = "1" * (c["1"] - 1) + "0" * c["0"] + "1"

        return max_odd
