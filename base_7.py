class Solution:
    def convertToBase7(self, num: int) -> str:
        """Converts an integer to its base 7 string representation.

        Args:
            num (int): The integer in base 10 to be converted.

        Returns:
            str: The base 7 representation of num as a string.

        Example:
            >>> convertToBase7(100)
            '202'
            >>> convertToBase7(-7)
            '-10'

        Time complexity: O(log_7(num)), where num is the absolute value of the input number.
        Space complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        base_7 = ""
        negative = False

        if num < 0:
            num *= -1
            negative = True

        while num >= 7:
            base_7 += str(num % 7)
            num //= 7

        base_7 += str(num)

        return "-" + base_7[::-1] if negative else base_7[::-1]
