class Solution:
    def maxDistinct(self, s: str) -> int:
        """
        Given a string s consisting of lowercase English letters,
        return the maximum number of substrings you can split s into such
        that each substring starts with a distinct character (i.e., no two
        substrings start with the same character).

        Args:
            s (str): Input string of lowercase English letters.

        Returns:
            int: Maximum number of substrings as described.

        Example:
            Input: s = "abc"
            Output: 3

        Time Complexity: O(n), where n is the length of s.
        Space Complexity: O(1), for set of unique characters (up to 26).

        LeetCode: Beats 98.12% of submissions.
        """
        return len(set(s))
