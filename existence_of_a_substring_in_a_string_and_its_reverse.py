class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        """
        Checks if there exists any substring of length 2 in the given string `s` that is also present in the reverse of `s`.

        Args:
            s (str): The input string.

        Returns:
            bool: True if such a substring exists, False otherwise.

        Example:
            >>> isSubstringPresent("abcba")
            True

        Time Complexity: O(n^2), where n is the length of the string.
        Space Complexity: O(n)

        LeetCode: Beats 100% of submissions
        """
        r_s = s[::-1]

        for i in range(len(s) - 1):
            if s[i : i + 2] in r_s:
                return True

        return False
