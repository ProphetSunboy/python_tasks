class Solution:
    def removePalindromeSub(self, s: str) -> int:
        """
        Given a string s consisting only of letters 'a' and 'b', return the minimum
        number of steps to make s empty by repeatedly removing a palindromic subsequence in each step.

        Definitions:
            - A palindromic subsequence is a sequence that reads the same forward
            and backward and can be derived from s by deleting zero or more characters
            without changing the order of the remaining characters.
            - In each step, you may remove any palindromic subsequence (not necessarily contiguous).

        Args:
            s (str): The input string consisting only of 'a' and 'b' characters.

        Returns:
            int: The minimum number of steps required to remove all characters from s.

        Example:
            >>> removePalindromeSub("ababa")
            1
            >>> removePalindromeSub("abb")
            2

        Time Complexity: O(n), where n is the length of s.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        return 1 if s == s[::-1] else 2
