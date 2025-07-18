class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        """Determines if the two halves of a given even-length string are alike,
        meaning they contain the same number of vowels (case-insensitive).

        Args:
            s (str): The input string of even length.

        Returns:
            bool: True if both halves have the same number of vowels, False otherwise.

        Example:
            >>> halvesAreAlike("book")
            True

        Time complexity: O(n), where n is the length of s.
        Space complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        a, b = s[: len(s) // 2], s[len(s) // 2 :]
        a_vow, b_vow = 0, 0

        for ch in a:
            if ch in vowels:
                a_vow += 1

        for ch in b:
            if ch in vowels:
                b_vow += 1

        return a_vow == b_vow
