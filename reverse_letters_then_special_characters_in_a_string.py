class Solution:
    def reverseByType(self, s: str) -> str:
        """
        Given a string `s` consisting of lowercase English letters and special
        characters, perform the following in order:

        1. Reverse the lowercase letters and place them back into the positions
        originally occupied by letters.
        2. Reverse the special characters and place them back into the positions
        originally occupied by special characters.

        Return the resulting string after performing these reversals.

        Args:
            s (str): Input string consisting of lowercase letters and special
            characters.

        Returns:
            str: The transformed string with letters and special characters
            reversed within their respective positions.

        Example:
            Input: s = "a,b$c"
            Output: "c$b,a"

        Time Complexity: O(n), where n is the length of the string.
        Space Complexity: O(n), for storing the letters and special characters.

        LeetCode: Beats 100% of submissions
        """
        letters = []
        special = []

        for ch in s:
            if ch.isalpha():
                letters.append(ch)
            else:
                special.append(ch)

        res = ""
        for ch in s:
            if ch.isalpha():
                res += letters.pop()
            else:
                res += special.pop()

        return res
