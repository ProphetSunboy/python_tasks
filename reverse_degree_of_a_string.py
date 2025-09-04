class Solution:
    def reverseDegree(self, s: str) -> int:
        """
        Calculates the reverse degree of a string.

        The reverse degree is defined as the sum over all characters in the string,
        where for each character, you multiply its position in the reversed alphabet
        ('a' = 26, 'b' = 25, ..., 'z' = 1) by its 1-based position in the string.

        Args:
            s (str): The input string consisting of lowercase English letters.

        Returns:
            int: The reverse degree of the string.

        Example:
            >>> reverseDegree("abc")
            148  # (26*1 + 25*2 + 24*3)

        Time Complexity: O(n), where n is the length of the input string.
        Space Complexity: O(1)

        LeetCode: Beats 97.82% of submissions
        """
        reverse_degree = 0

        for i, ch in enumerate(s):
            reverse_degree += (97 + 26 - ord(ch)) * (i + 1)

        return reverse_degree
