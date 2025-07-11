class Solution:
    def greatestLetter(self, s: str) -> str:
        """Finds the greatest English letter present in both uppercase and lowercase forms in the input string.

        The function returns the greatest such letter in uppercase. If no such letter exists, returns an empty string.
        A letter is considered greater if it appears later in the English alphabet.

        Args:
            s (str): The input string containing English letters.

        Returns:
            str: The greatest English letter (in uppercase) present in both cases, or an empty string if none exists.

        Example:
            >>> greatestLetter("lEeTcOdE")
            'E'
            >>> greatestLetter("abcde")
            ''

        Time complexity: O(n), where n is the length of the input string.
        Space complexity: O(1), as the auxiliary storage for the alphabet is constant.

        LeetCode: Beats 100% of submissions
        """
        alph = [[False, False] for _ in range(26)]

        for ch in set(s):
            if ch.islower():
                alph[ord(ch) - 97][0] = True
            else:
                alph[ord(ch.lower()) - 97][1] = True

        for i in range(len(alph) - 1, -1, -1):
            if all(alph[i]):
                return chr(i + 97).upper()

        return ""
