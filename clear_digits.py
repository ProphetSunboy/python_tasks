class Solution:
    def clearDigits(self, s: str) -> str:
        """
        Removes all digits from the input string `s` by repeatedly performing the following operation:
        - Delete the first digit and the closest non-digit character to its left.

        The operation cannot be performed on a digit that does not have any non-digit character to its left.

        Args:
            s (str): The input string containing digits and non-digit characters.

        Returns:
            str: The resulting string after all possible operations have been performed.

        Example:
            >>> clearDigits("abc1d2")
            'ab'

        Time complexity: O(n), where n is the length of s.
        Space complexity: O(n).

        LeetCode: Beats 100% of submissions
        """
        stack = []

        for ch in s:
            if ch.isalpha():
                stack.append(ch)
            else:
                stack.pop()

        return "".join(stack)
