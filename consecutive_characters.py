class Solution:
    def maxPower(self, s: str) -> int:
        """Given a string s, return its power - the maximum length of a non-empty substring
        containing only one unique character.

        Args:
            s (str): Input string

        Returns:
            int: The power of the string s

        Example:
            >>> maxPower("leetcode")
            2
            >>> maxPower("abbcccddddeeeeedcba")
            5

        Time complexity: O(n) where n is the length of the string
        Space complexity: O(1) since we only use a few variables

        LeetCode: Beats 100% of submissions
        """
        s_power = 0
        temp_p = 0
        curr_ch = s[0]

        for ch in s:
            if ch == curr_ch:
                temp_p += 1
            else:
                if temp_p > s_power:
                    s_power = temp_p

                curr_ch = ch
                temp_p = 1

        if temp_p > s_power:
            s_power = temp_p

        return s_power
