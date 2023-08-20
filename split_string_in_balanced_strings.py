class Solution:
    def balancedStringSplit(self, s: str) -> int:
        """
        Return the maximum number of balanced strings that can be obtained.

        Balanced strings are those that have an equal quantity of 'L' and 'R'
        characters.

        Given a balanced string s, split it into some number of substrings such
        that:

            Each substring is balanced.

        :param str s: balanced string
        :returns int balanced_strings: maximum number of balanced strings that
        can be obtained

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 98.33%
        """
        stack = []
        balanced_strings = 0

        for ch in s:
            if stack:
                if stack[-1] != ch:
                    stack.pop()

                    if not stack:
                        balanced_strings += 1
                else:
                    stack.append(ch)
            else:
                stack.append(ch)

        return balanced_strings
