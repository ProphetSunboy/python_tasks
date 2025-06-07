class Solution:
    def shift(self, ch: str, x: int) -> str:
        """Shifts a character by a specified number of positions in the alphabet.

        Args:
            ch (str): The input character to shift
            x (int): The number of positions to shift the character

        Returns:
            str: The shifted character

        Example:
            >>> shift('a', 1)
            'b'
            >>> shift('x', 0)
            'x'
        """
        return chr(ord(ch) + x)

    def replaceDigits(self, s: str) -> str:
        """Replaces all digits in a string with shifted characters based on the previous character.

        Given a 0-indexed string s containing lowercase English letters in even indices and digits in odd indices,
        replaces each digit s[i] with the character that is s[i] positions after the previous character s[i-1].

        Args:
            s (str): The input string containing alternating letters and digits

        Returns:
            str: The string with all digits replaced by their corresponding shifted characters

        Example:
            >>> replaceDigits("a1c1e1")
            'abcdef'

        Time complexity: O(n) - where n is the length of the string
        Space complexity: O(n) - for storing the result string

        LeetCode: Beats 100% of submissions
        """
        res = ""

        for i, ch in enumerate(s):
            if ch.isalpha():
                res += ch
            else:
                res += self.shift(s[i - 1], int(ch))

        return res
