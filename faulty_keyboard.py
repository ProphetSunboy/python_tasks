class Solution:
    def finalString(self, s: str) -> str:
        """Simulates typing a string on a faulty keyboard where every time the character 'i' is typed,
        the current string is reversed. All other characters are appended as normal.

        Args:
            s (str): The input string to type using the faulty keyboard.

        Returns:
            str: The final string displayed after processing all characters in s.

        Example:
            >>> finalString("string")
            'rtsng'
            >>> finalString("poiinter")
            'ponter'

        Time complexity: O(n^2) in the worst case due to repeated reversals.
        Space complexity: O(n), where n is the length of s.

        LeetCode: Beats 100% of submissions
        """
        res = ""

        for ch in s:
            if ch == "i":
                res = res[::-1]
            else:
                res += ch

        return res
