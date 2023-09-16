class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
        Given a binary string s, return the number of non-empty substrings that
        have the same number of 0's and 1's, and all the 0's and all the 1's in
        these substrings are grouped consecutively.

        Substrings that occur multiple times are counted the number of times
        they occur.

        :param str s: binary string
        :returns int alterating_bits: number of non-empty substrings that have
        the same number of 0's and 1's, and all the 0's and all the 1's in these
        substrings are grouped consecutively

        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 97.66%
        """
        last = -1
        tot = 0
        count = 0
        lastcount = 0
        for i in s:
            if last != i:
                tot += min(count, lastcount)
                lastcount = count
                count = 1
                last = i
            else:
                count += 1
        tot += min(count, lastcount)
        return tot
