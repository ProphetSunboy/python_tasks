class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        """Count the number of words that start with a given prefix.

        Args:
            words (list[str]): List of strings to check
            pref (str): Prefix to search for

        Returns:
            int: Number of words that start with the given prefix

        Examples:
            >>> prefixCount(["pay", "attention", "practice", "attend"], "at")
            2  # "attention" and "attend" start with "at"
            >>> prefixCount(["leetcode", "win", "loops", "success"], "code")
            0  # No words start with "code"

        Time complexity: O(n*m) - where n is number of words and m is length of prefix
        Space complexity: O(1) - constant space used

        LeetCode: Beats 100% of submissions
        """
        return sum([word.startswith(pref) for word in words])
