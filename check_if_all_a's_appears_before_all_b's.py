class Solution:
    def checkString(self, s: str) -> bool:
        """
        Checks if every 'a' in the string appears before every 'b'.

        Args:
            s (str): Input string consisting only of 'a' and 'b'.

        Returns:
            bool: True if all 'a's appear before any 'b', False otherwise.

        Example:
            >>> checkString("aaabbb")
            True
            >>> checkString("abab")
            False

        Time Complexity: O(n), where n is the length of s.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        b = False

        for ch in s:
            if ch == "a" and b:
                return False
            elif ch == "b":
                b = True

        return True
