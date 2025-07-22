class Solution:
    def repeatedCharacter(self, s: str) -> str:
        """Returns the first letter to appear twice in the given string.

        Given a string `s` consisting of lowercase English letters, this function finds and returns
        the first character that appears more than once when traversing the string from left to right.

        Args:
            s (str): The input string of lowercase English letters.

        Returns:
            str: The first letter to appear twice.

        Example:
            >>> repeatedCharacter("abccbaacz")
            'c'
            # 'c' is the first letter to appear twice.

        Time complexity: O(n), where n is the length of s.
        Space complexity: O(1), since the set of lowercase letters is bounded.

        LeetCode: Beats 100% of submissions
        """
        seen = set()

        for ch in s:
            if ch not in seen:
                seen.add(ch)
            else:
                return ch
