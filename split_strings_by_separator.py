class Solution:
    def splitWordsBySeparator(self, words: list[str], separator: str) -> list[str]:
        """
        Splits each string in the input list by the given separator and returns
        a list of all resulting non-empty substrings.

        Args:
            words (list[str]): List of input strings to split.
            separator (str): The character used to split each string.

        Returns:
            list[str]: List of non-empty substrings, preserving the original order.

        Notes:
            - The separator is not included in the resulting substrings.
            - Splitting may result in more than two substrings per word.
            - Empty substrings resulting from consecutive separators or leading/trailing separators are excluded from the result.

        Example:
            >>> splitWordsBySeparator(["one.two", "three", "four.five"], ".")
            ['one', 'two', 'three', 'four', 'five']

        Time Complexity: O(N), where N is the total number of characters in all words.
        Space Complexity: O(M), where M is the total number of non-empty substrings returned.

        LeetCode: Beats 100% of submissions
        """
        res = []

        for word in words:
            for w in word.split(separator):
                if w != "":
                    res.append(w)

        return res
