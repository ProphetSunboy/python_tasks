class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        """
        A valid parentheses string is either empty "", "(" + A + ")", or A + B,
        where A and B are valid parentheses strings, and + represents string
        concatenation.

            For example, "", "()", "(())()", and "(()(()))" are all valid
            parentheses strings.

        A valid parentheses string s is primitive if it is nonempty, and there
        does not exist a way to split it into s = A + B, with A and B nonempty
        valid parentheses strings.

        Given a valid parentheses string s, consider its primitive
        decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid
        parentheses strings.

        Return s after removing the outermost parentheses of every primitive
        string in the primitive decomposition of s.

        :param str s: valid parentheses string
        :returns str ans: s after removing the outermost parentheses of every
        primitive string in the primitive decomposition of s

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 99.08%
        """
        ans = ""
        o, c = 0, 0
        dec = ""

        for par in s:
            if par == "(":
                o += 1
            else:
                c += 1

            dec += par
            if o == c:
                ans += dec[1:-1]
                dec = ""
                o = c = 0

        return ans
