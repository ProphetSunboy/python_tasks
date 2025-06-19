class Solution:
    def maxDepth(self, s: str) -> int:
        """Calculate the maximum nesting depth of parentheses in a valid string.

        The nesting depth is defined as the maximum number of parentheses that are open at the same time.

        Args:
            s (str): A valid parentheses string.

        Returns:
            int: The maximum nesting depth of the parentheses.

        Examples:
            >>> maxDepth("(1+(2*3)+((8)/4))+1")
            3
            >>> maxDepth("(1)+((2))+(((3)))")
            3
            >>> maxDepth("1+(2*3)/(2-1)")
            1
            >>> maxDepth("1")
            0

        Time complexity: O(N), where N is the length of the string s.
        Space complexity: O(N), due to the stack used for tracking open parentheses.

        LeetCode: Beats 100% of submissions
        """
        max_depth = 0
        stack = []

        for ch in s:
            if ch == "(":
                stack.append("(")

                if len(stack) > max_depth:
                    max_depth = len(stack)
            elif ch == ")":
                stack.pop()

        return max_depth
