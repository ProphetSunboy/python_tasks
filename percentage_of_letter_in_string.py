class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        """Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to the nearest whole percent.

        Args:
            s (str): The input string to check
            letter (str): The character to count in the string

        Returns:
            int: The percentage of characters that equal letter, rounded down to nearest whole percent

        Example:
            >>> percentageLetter("foobar", "o")
            33

        Time complexity: O(n) - where n is the length of the string
        Space complexity: O(1) - only using a single counter variable

        LeetCode: Beats 100% of submissions
        """
        return int(s.count(letter) / len(s) * 100)
