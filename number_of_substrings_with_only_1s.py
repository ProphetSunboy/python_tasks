class Solution:
    def numSub(self, s: str) -> int:
        """
        Given a binary string s, return the number of substrings with all characters '1'.
        Since the answer may be large, return it modulo 10^9 + 7.

        Args:
            s (str): A binary string.

        Returns:
            int: The number of substrings consisting only of '1's, modulo 10^9 + 7.

        Example:
            Input:  s = "0110111"
            Output: 9

            Explanation:
                Substrings containing only '1's are:
                "1", "1", "1", "11", "11", "111", "1", "11", "1"
                (Total: 9)

        Time Complexity: O(n), where n is the length of s.
        Space Complexity: O(n), for splitting the string.

        LeetCode: Beats 98.88% of submissions
        """
        res = 0
        i = 0
        s = s.split("0")

        for sub_s in s:
            if sub_s:
                res += (len(sub_s) * (len(sub_s) + 1)) // 2

        return res % (10**9 + 7)
