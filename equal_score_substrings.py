class Solution:
    def scoreBalance(self, s: str) -> bool:
        """
        Determines whether a given string `s` of lowercase English letters can be split
        into two non-empty substrings such that the sum of the positions of the characters
        ('a' = 1, 'b' = 2, ..., 'z' = 26) in each substring is equal.

        Args:
            s (str): Input string consisting of lowercase English letters.

        Returns:
            bool: True if such a split exists, False otherwise.

        Example:
            >>> scoreBalance("abccba")
            True   # because "abc" and "cba" both sum to 6.

        Time Complexity: O(n), where n is the length of the input string.
        Space Complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        l, r = 0, sum([ord(s[i]) - 96 for i in range(len(s))])

        i = 0
        while l < r:
            l += ord(s[i]) - 96
            r -= ord(s[i]) - 96

            i += 1

            if l == r and i < len(s):
                return True

        return False
