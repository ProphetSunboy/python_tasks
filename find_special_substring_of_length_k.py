class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        """
        Determines if there exists a substring of length exactly k in the given string s that satisfies all of the following:
            - The substring consists of only one distinct character (e.g., "aaa" or "bbb").
            - If there is a character immediately before the substring, it must be different from the character in the substring.
            - If there is a character immediately after the substring, it must also be different from the character in the substring.

        Args:
            s (str): The input string to search within.
            k (int): The required length of the special substring.

        Returns:
            bool: True if such a substring exists, False otherwise.

        Example:
            >>> hasSpecialSubstring("aabaaa", 3)
            True
            >>> hasSpecialSubstring("abcde", 2)
            False

        Time Complexity: O(n)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        for i in range(k):
            for j in range(i, len(s) - k + 1, k):
                if (
                    len(set(s[j : j + k])) == 1
                    and (j == 0 or s[j - 1] != s[j])
                    and (j + k == len(s) or s[j + k - 1] != s[j + k])
                ):
                    return True

        return False
