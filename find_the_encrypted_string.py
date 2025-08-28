class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        """
        Encrypts the input string s by shifting each character to the kth character ahead in a cyclic manner.

        For each character at index i in s, the encrypted character is s[(i + k) % len(s)].

        Args:
            s (str): Input string to encrypt.
            k (int): Number of positions to shift each character.

        Returns:
            str: The encrypted string.

        Example:
            >>> getEncryptedString("abcde", 2)
            'cdeab'
            >>> getEncryptedString("hello", 1)
            'elloh'

        Time Complexity: O(n), where n is the length of s.
        Space Complexity: O(n)

        LeetCode: Beats 100% of submissions
        """
        enc = ""

        for i in range(len(s)):
            enc += s[(i + k) % len(s)]

        return enc
