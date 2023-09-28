class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return True if they are equal when both are
        typed into empty text editors. '#' means a backspace character.

        Note that after backspacing an empty text, the text will continue empty.

        :param str s: string
        :param str t: string
        :returns bool equal: s and t are equal when both are typed into empty
        text editors

        Time complexity: O(n+m)
        Space complexity: O(n+m)

        LeetCode: Beats 99.27%
        """
        stack_s = []
        stack_t = []

        for ch in s:
            if ch == "#":
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(ch)

        for ch in t:
            if ch == "#":
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(ch)

        return stack_s == stack_t
