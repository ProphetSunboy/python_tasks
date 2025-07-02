class Solution:
    def thousandSeparator(self, n: int) -> str:
        """Given an integer n, return a string representation of n with dots (".") as thousands separators.

        Args:
            n (int): The integer to format.

        Returns:
            str: The formatted string with thousands separators.

        Example:
            >>> thousandSeparator(123456789)
            '123.456.789'
            >>> thousandSeparator(1000)
            '1.000'
            >>> thousandSeparator(987)
            '987'

        LeetCode: Beats 100% of submissions
        """
        s = str(n)
        curr = 0
        res = ""

        for i in range(len(s) - 1, -1, -1):
            if curr == 3:
                res += "." + s[i]
                curr = 1
            else:
                res += s[i]
                curr += 1

        return res[::-1]
