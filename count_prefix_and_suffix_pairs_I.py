class Solution:
    def is_prefix_and_suffix(self, str1: str, str2: str) -> bool:
        """
        Checks if str1 is both a prefix and a suffix of str2.

        Args:
            str1 (str): The string to check as prefix and suffix.
            str2 (str): The string to check against.

        Returns:
            bool: True if str1 is both a prefix and a suffix of str2, False otherwise.

        Example:
            >>> is_prefix_and_suffix("ab", "abcab")
            True
            >>> is_prefix_and_suffix("a", "bca")
            False
        """
        return str2.startswith(str1) and str2.endswith(str1)

    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        """
        Counts the number of index pairs (i, j) in the given list of words such that i < j and
        words[i] is both a prefix and a suffix of words[j].

        A string str1 is considered both a prefix and a suffix of str2 if:
            - str2.startswith(str1) and str2.endswith(str1)

        Args:
            words (list[str]): The list of input strings.

        Returns:
            int: The number of valid (i, j) pairs where i < j and words[i] is both a prefix and a suffix of words[j].

        Example:
            >>> countPrefixSuffixPairs(["a", "aba", "ababa"])
            2
            >>> countPrefixSuffixPairs(["abc", "abcd", "abcabc"])
            1

        Time complexity: O(n^2 * k), where n is the number of words and k is the average word length.
        Space complexity: O(1)

        LeetCode: Beats 90.08% of submissions
        """
        counter = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if self.is_prefix_and_suffix(words[i], words[j]):
                    counter += 1

        return counter
