class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        """Counts how many strings in the list `patterns` appear as substrings in the string `word`.

        A substring is a contiguous sequence of characters within a string.

        Args:
            patterns (list[str]): List of string patterns to search for.
            word (str): The string in which to search for patterns.

        Returns:
            int: The number of patterns that appear as substrings in `word`.

        Example:
            >>> numOfStrings(["a", "abc", "bc"], "abc")
            3
            >>> numOfStrings(["a", "b", "c"], "aaaaabbbbb")
            2

        Time complexity: O(m * n), where m is the number of patterns and n is the length of `word`.
        Space complexity: O(1), not counting input and output.

        LeetCode: Beats 100% of submissions
        """
        return sum([pattern in word for pattern in patterns])
