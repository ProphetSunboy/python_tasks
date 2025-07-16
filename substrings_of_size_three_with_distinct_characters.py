class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        """Counts the number of good substrings of length three in the given string.

        A substring is considered "good" if all its characters are distinct.

        Args:
            s (str): The input string.

        Returns:
            int: The number of good substrings of length three.

        Example:
            >>> countGoodSubstrings("xyzzaz")
            1
            >>> countGoodSubstrings("aababcabc")
            4

        Time complexity: O(n), where n is the length of s.
        Space complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        good = 0

        for i in range(len(s) - 2):
            if s[i] != s[i + 1] and s[i] != s[i + 2] and s[i + 1] != s[i + 2]:
                good += 1

        return good
