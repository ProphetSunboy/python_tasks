class FirstSolution:
    def bitwiseComplement(self, n: int) -> int:
        """
        Given an integer n, return its complement.

        The complement of an integer is the integer you get when you flip all
        the 0's to 1's and all the 1's to 0's in its binary representation.

        For example, The integer 5 is "101" in binary and its complement is
        "010" which is the integer 2.

        :param int n: integer
        :returns int complement: complement of n

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 96.80%
        """
        flips = ["1", "0"]
        complement = ""
        bin_n = bin(n)[2:]

        for ch in bin_n:
            complement += flips[ch == "1"]

        return int(complement, 2)


class SecondSolution:
    def bitwiseComplement(self, n: int) -> int:
        bin_n = bin(n)[2:]

        return int(bin_n.translate(str.maketrans("01", "10")), 2)
