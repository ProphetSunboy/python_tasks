class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        """
        Remove all trailing vowels from the given lowercase English string.

        A vowel is one of: 'a', 'e', 'i', 'o', 'u'.

        Args:
            s (str): Input string consisting of lowercase English letters.

        Returns:
            str: The string with trailing vowels removed.

        Example:
            Input: "heallo"
            Output: "heall"

        Time Complexity: O(n), since we iterate over the string once.
        Space Complexity: O(1), as constant extra space is used.

        LeetCode: Beats 100% of submissions
        """
        i = len(s) - 1

        while i >= 0:
            if s[i] in "aeiou":
                i -= 1
            else:
                break

        return s[: i + 1]
