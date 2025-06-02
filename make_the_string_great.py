class Solution:
    def makeGood(self, s: str) -> str:
        """Given a string s of lower and upper case English letters.

        A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:
        - 0 <= i <= s.length - 2
        - s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.

        To make the string good, you can choose two adjacent characters that make the string bad and remove them.
        You can keep doing this until the string becomes good.

        Args:
            s (str): Input string containing lower and upper case English letters

        Returns:
            str: The string after making it good. Empty string is also considered good.

        Example:
            >>> makeGood("leEeetcode")
            "leetcode"
            >>> makeGood("abBAcC")
            ""

        Time complexity: O(n) where n is the length of the string
        Space complexity: O(n) to store the stack

        LeetCode: Beats 100% of submissions
        """
        result = [s[0]]

        for i in range(1, len(s)):
            if result and s[i].lower() == result[-1].lower() and s[i] != result[-1]:
                result.pop()
            else:
                result.append(s[i])

        return "".join(result)
