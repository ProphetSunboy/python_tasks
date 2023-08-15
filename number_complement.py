class Solution:
    def findComplement(self, num: int) -> int:
        """
        Given an integer num, return its complement.

        The complement of an integer is the integer you get when you flip all
        the 0's to 1's and all the 1's to 0's in its binary representation.

        For example, The integer 5 is "101" in binary and its complement is
        "010" which is the integer 2.


        :param int num: integer number
        :returns int complement: number complement


        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 96.80%
        """
        complement = 0
        bins = [0, 1]

        for i, ch in enumerate(bin(num)[2:][::-1]):
            complement += bins[ch == "0"] * (2**i)

        return complement
