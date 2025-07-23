class Solution:
    def countPrefixes(self, words: list[str], s: str) -> int:
        """Counts how many strings in the list `words` are prefixes of the string `s`.

        A prefix of a string is a substring that occurs at the beginning of the string.

        Args:
            words (List[str]): List of lowercase English strings.
            s (str): The target string to check prefixes against.

        Returns:
            int: The number of strings in `words` that are prefixes of `s`.

        Example:
            >>> countPrefixes(["a", "b", "ab", "abc"], "abc")
            3
            # "a", "ab", and "abc" are prefixes of "abc".

        Time complexity: O(n * m), where n is the number of words and m is the average length of the words.
        Space complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        prefixes = 0

        for word in words:
            if s.startswith(word):
                prefixes += 1

        return prefixes
