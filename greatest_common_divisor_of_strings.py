class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        For two strings s and t, we say "t divides s" if and only if
        s = t + ... + t (i.e., t is concatenated with itself one or more times).

        Given two strings str1 and str2, return the largest string x such that
        x divides both str1 and str2.

        :param str str1: string
        :param str str2: string
        :returns x: largest string x such that x divides both str1 and str2.

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 95.15%
        """
        if len(str1) < len(str2):
            min_s, max_s = str1, str2
        else:
            min_s, max_s = str2, str1

        x = min_s[::]

        while x:
            max_div = len(max_s) / len(x)
            if max_div % 1 == 0:
                if x * int(max_div) == max_s:
                    min_div = len(min_s) / len(x)
                    if min_div % 1 == 0:
                        if x * int(min_div) == min_s:
                            return x

            x = x[:-1]

        return ""
