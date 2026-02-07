class Solution:
    def minimumDeletions(self, s: str) -> int:
        """
        Given a string s consisting only of characters 'a' and 'b', return the
        minimum number of deletions needed to make s balanced.

        A string is balanced if there is no pair of indices (i, j) such that
        i < j, s[i] == 'b', and s[j] == 'a'.

        Args:
            s (str): Input string of characters 'a' and 'b'.

        Returns:
            int: Minimum number of deletions needed to make s balanced.

        Example:
            Input: s = "aababbab"
            Output: 2

        Time Complexity: O(n), where n is the length of s.
        Space Complexity: O(1)

        LeetCode: Beats 92.05% of submissions
        """
        deletions = 0
        b_count = 0

        for char in s:
            if char == "a":
                deletions = min(deletions + 1, b_count)
            else:
                b_count += 1

        return deletions
