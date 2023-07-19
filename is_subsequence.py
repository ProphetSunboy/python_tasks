class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return True if s is a subsequence of t,
        or False otherwise.

        A subsequence of a string is a new string that is formed from the
        original string by deleting some (can be none) of the characters without
        disturbing the relative positions of the remaining characters.
        (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

        LeetCode: Beats 97.96%        
        """
        if s == '':
            return True
        elif len(s) > len(t):
            return False

        j = 0

        for i in range(len(t)):
            if t[i] == s[j]:
                j += 1

                if j == len(s):
                    return True

        return False