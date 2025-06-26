class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        """Returns the sum of the digits of x if x is a Harshad number, otherwise returns -1.

        A Harshad number is an integer that is divisible by the sum of its digits.

        Args:
            x (int): The integer to check.

        Returns:
            int: The sum of the digits of x if x is a Harshad number, otherwise -1.

        Example:
            >>> sumOfTheDigitsOfHarshadNumber(18)
            9
            >>> sumOfTheDigitsOfHarshadNumber(19)
            -1

        LeetCode: Beats 100% of submissions
        """
        digit_sum = sum(map(int, list(str(x))))

        return digit_sum if x % digit_sum == 0 else -1
