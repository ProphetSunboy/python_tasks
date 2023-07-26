class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        """
        Given a binary string s, return True if the longest contiguous segment
        of 1's is strictly longer than the longest contiguous segment of 0's
        in s, or return False otherwise.

        For example, in s = "110100010" the longest continuous segment of 1s
        has length 2, and the longest continuous segment of 0s has length 3.

        LeetCode: Beats 94.20%
        """
        longest_ones = 0
        longest_zeros = 0

        local_ones = 0
        local_zeros = 0
        for el in s:
            if el == "1":
                local_zeros = 0
                local_ones += 1

                if local_ones > longest_ones:
                    longest_ones = local_ones

            else:
                local_ones = 0
                local_zeros += 1

                if local_zeros > longest_zeros:
                    longest_zeros = local_zeros

        return longest_ones > longest_zeros
