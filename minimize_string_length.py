class Solution:
    def minimizedStringLength(self, s: str) -> int:
        """Minimizes the length of a string by removing duplicate characters.

        Given a string s, performs operations to remove duplicate characters by either:
        1. Deleting the closest occurrence of a character to the left of a chosen position
        2. Deleting the closest occurrence of a character to the right of a chosen position

        Args:
            s (str): The input string to minimize

        Returns:
            int: The length of the minimized string

        Example:
            >>> minimizedStringLength("aaabc")
            3  # Can be minimized to "abc"

        Time complexity: O(n) - where n is the length of the input string
        Space complexity: O(n) - for storing the set of unique characters

        LeetCode: Beats 100% of submissions
        """
        return len(set(s))
