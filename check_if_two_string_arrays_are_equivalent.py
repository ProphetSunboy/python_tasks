class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        """
        Determines if two string lists represent the same string.

        Concatenates the elements of each list in order and compares the resulting strings.

        Args:
            word1 (list[str]): First list of strings.
            word2 (list[str]): Second list of strings.

        Returns:
            bool: True if strings are equal, False otherwise.

        Examples:
            >>> arrayStringsAreEqual(["ab", "c"], ["a", "bc"])
            True
            >>> arrayStringsAreEqual(["a", "cb"], ["ab", "c"])
            False

        Time complexity: O(N), where N is the total number of characters in both lists.
        Space complexity: O(N), due to string concatenation.

        LeetCode: Beats 100% of submissions
        """
        return "".join(word1) == "".join(word2)
