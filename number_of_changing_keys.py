class Solution:
    def countKeyChanges(self, s: str) -> int:
        """Counts the number of key changes in a given string.

        A key change occurs when a character is different from the preceding one,
        ignoring case. For example, in "aAbBcC", there are two key changes:
        from 'A' to 'b' and from 'B' to 'c'.

        Args:
            s (str): The string typed by the user.

        Returns:
            int: The total number of key changes.

        Example:
            >>> countKeyChanges("aAbBcC")
            2
            >>> countKeyChanges("Aa")
            0

        LeetCode: Beats 100% of submissions
        """
        key_changes = 0

        for i in range(1, len(s)):
            if s[i].lower() != s[i - 1].lower():
                key_changes += 1

        return key_changes
