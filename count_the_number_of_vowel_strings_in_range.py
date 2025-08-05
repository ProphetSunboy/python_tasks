class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        """
        Counts the number of "vowel strings" in a sublist of words.

        A "vowel string" is defined as a string that starts and ends with a vowel character
        ('a', 'e', 'i', 'o', 'u').

        Args:
            words (list[str]): List of strings to check.
            left (int): Left index of the inclusive range.
            right (int): Right index of the inclusive range.

        Returns:
            int: Number of vowel strings in words[left:right+1].

        Example:
            >>> vowelStrings(["aba", "bcb", "ece", "aa", "e"], 0, 2)
            2

        Time complexity: O(n), where n is the size of the range [left, right].
        Space complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        vowels = {"a", "e", "i", "o", "u"}
        vowel_strings = 0

        for i in range(left, right + 1):
            if words[i][0] in vowels and words[i][-1] in vowels:
                vowel_strings += 1

        return vowel_strings
