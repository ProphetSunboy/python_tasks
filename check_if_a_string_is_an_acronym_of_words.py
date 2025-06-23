class Solution:
    def isAcronym(self, words: list[str], s: str) -> bool:
        """Checks if a string is a valid acronym of a list of words.

        An acronym is formed by concatenating the first character of each word in order.

        Args:
            words (list[str]): List of words to check.
            s (str): The string to validate as an acronym.

        Returns:
            bool: True if s is a valid acronym of words, False otherwise.

        Example:
            >>> isAcronym(["hello", "world"], "hw")
            True
            >>> isAcronym(["hello", "world"], "hw!")
            False

        Time complexity: O(N), where N is the total length of all words.
        Space complexity: O(1), only storing the acronym string.

        LeetCode: Beats 100% of submissions
        """
        return "".join([word[0] for word in words]) == s
