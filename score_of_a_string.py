class Solution:
    def scoreOfString(self, s: str) -> int:
        """Calculates the score of a string.

        The score of a string is defined as the sum of the absolute
        differences between the ASCII values of adjacent characters.

        Args:
            s (str): The input string.

        Returns:
            int: The score of the string.

        Example:
            >>> scoreOfString("hello")
            13

        LeetCode: Beats 100% of submissions
        """
        score = 0

        for i in range(len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i + 1]))

        return score
