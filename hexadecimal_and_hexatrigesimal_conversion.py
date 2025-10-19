class Solution:
    def hexatrig(self, num):
        """
        Converts an integer to its hexatrigesimal (base-36) string representation, using
        digits 0-9 and lowercase letters a-z.

        Args:
            num (int): The integer to convert. Should be non-negative.

        Returns:
            str: The base-36 (hexatrigesimal) representation of num as a string. If num is 0, returns '0'.

        Example:
            >>> hexatrig(0)
            '0'
            >>> hexatrig(35)
            'z'
            >>> hexatrig(36)
            '10'
            >>> hexatrig(12345)
            '9ix'
        """
        if num == 0:
            return "0"

        chars = "0123456789abcdefghijklmnopqrstuvwxyz"
        base36_str = ""

        while num > 0:
            remainder = num % 36
            base36_str = chars[remainder] + base36_str
            num //= 36

        return base36_str

    def concatHex36(self, n: int) -> str:
        """
        Given an integer n, return the concatenation of the hexadecimal representation of n squared (n^2)
        and the hexatrigesimal (base-36) representation of n cubed (n^3).

        - The hexadecimal (base-16) system uses digits 0–9 and uppercase letters A–F to represent values 0–15.
        - The hexatrigesimal (base-36) system uses digits 0–9 and uppercase letters A–Z to represent values 0–35.

        Args:
            n (int): Input integer.

        Returns:
            str: Concatenation of the hexadecimal string of n^2 and the base-36 string of n^3 (both in uppercase).

        Example:
            >>> concatHex36(10)
            '64RS'

        Time Complexity: O(log(n))
        Space Complexity: O(log(n))

        LeetCode: Beats 100% of submissions
        """
        return hex(n**2)[2:].upper() + self.hexatrig(n**3).upper()
