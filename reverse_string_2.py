class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """
        Given a string s and an integer k, reverse the first k characters for
        every 2k characters counting from the start of the string.

        If there are fewer than k characters left, reverse all of them. If there
        are less than 2k but greater than or equal to k characters, then reverse
        the first k characters and leave the other as original.

        :param str s: original string
        :param int k: group size
        :returns str res: edited string, according to given condition

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 95.51%
        """
        res = ""

        for i in range(0, len(s), 2 * k):
            temp = s[i : i + 2 * k]

            if len(temp) < k:
                res += temp[::-1]
            else:
                res += temp[:k][::-1] + temp[k:]

        return res
