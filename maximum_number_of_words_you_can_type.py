class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        """Given a string text of words separated by a single space and a string
        brokenLetters of distinct broken letter keys, return the number of words that can be fully typed.

        Args:
            text (str): A string of words separated by single spaces (no leading/trailing spaces).
            brokenLetters (str): A string of distinct broken letter keys.

        Returns:
            int: The number of words that can be fully typed without using broken letters.

        Example:
            >>> canBeTypedWords("hello world", "ad")
            1
            >>> canBeTypedWords("leet code", "lt")
            1
            >>> canBeTypedWords("leet code", "e")
            0

        Time complexity: O(n * m) where n is number of words and m is average word length
        Space complexity: O(1) excluding input strings

        LeetCode: Beats 100% of submissions
        """
        counter = 0

        for word in text.split():
            if set(word).intersection(brokenLetters):
                continue

            counter += 1

        return counter
