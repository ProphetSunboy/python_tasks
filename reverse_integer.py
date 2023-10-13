class Solution:
    def reverse(self, x: int) -> int:
        """
        Given a signed 32-bit integer x, return x with its digits reversed. If
        reversing x causes the value to go outside the signed 32-bit integer
        range [-2^31, 2^31 - 1], then return 0.

        Assume the environment does not allow you to store 64-bit integers
        (signed or unsigned).

        :param int x: signed 32-bit integer x
        :returns int res: x with its digits reversed

        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 99.26%
        """
        negative = x < 0
        x = abs(x)
        n = x
        i = -1
        while n >= 1:
            i += 1
            n /= 10

        res = 0
        while x >= 1:
            x, m = divmod(x, 10)
            res += m * 10**i
            i -= 1

        if res > 2**31 - 1:
            return 0

        return -res if negative else res
