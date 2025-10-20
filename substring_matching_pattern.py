class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        """
        Determines if the pattern string `p` (which contains exactly one '*' character) can be made a substring of `s`
        by replacing the '*' in `p` with any (possibly empty) sequence of characters.

        Args:
            s (str): The string to search within.
            p (str): The pattern containing exactly one '*' wildcard.

        Returns:
            bool: True if by expanding the '*' the resulting string is a substring of `s`, False otherwise.

        Example:
            >>> hasMatch("abacaba", "ab*a")
            True
            >>> hasMatch("foobar", "f*r")
            True
            >>> hasMatch("python", "y*nz")
            False

        Time Complexity: O(n), where n is the length of s.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        pattern = p.split("*")

        try:
            l = s.index(pattern[0])
            r = s.index(pattern[1], l + len(pattern[0]))

        except ValueError:
            return False

        return True
