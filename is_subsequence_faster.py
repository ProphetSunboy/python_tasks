class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return True if s is a subsequence of t, or
        False otherwise.

        A subsequence of a string is a new string that is formed from the
        original string by deleting some (can be none) of the characters without
        disturbing the relative positions of the remaining characters.
        (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

        :param str s: string
        :param str t: string
        :returns bool is_sub: s is subsequence of t

        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 98.95%
        """
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1

            j += 1

        return i == len(s)
