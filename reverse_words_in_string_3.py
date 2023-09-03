class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Given a string s, reverse the order of characters in each word within a
        sentence while still preserving whitespace and initial word order.

        :param str s: original string
        :returns str res: s with reversed words

        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 99.73%
        """
        return " ".join(map(lambda x: x[::-1], s.split()))
