# First solution
class Solution:
    def is_digit_sum_even(self, num: int) -> bool:
        """Determines if the sum of the digits of a given integer is even.

        Args:
            num (int): The integer whose digits will be summed.

        Returns:
            bool: True if the sum of the digits is even, False otherwise.

        Example:
            >>> is_digit_sum_even(123)
            True
            >>> is_digit_sum_even(124)
            False
        """
        digit_sum = 0

        while num > 0:
            digit_sum += num % 10
            num //= 10

        return digit_sum % 2 == 0

    def countEven(self, num: int) -> int:
        """Counts the number of positive integers less than or equal to `num` whose digit sums are even.

        The digit sum of a positive integer is the sum of all its digits.

        Args:
            num (int): The upper bound integer.

        Returns:
            int: The count of positive integers ≤ num with an even digit sum.

        Example:
            >>> countEven(4)
            2
            >>> countEven(30)
            14

        Time complexity: O(n), where n is the value of num.
        Space complexity: O(1).
        """
        counter = 0

        for n in range(1, num + 1):
            counter += self.is_digit_sum_even(n)

        return counter


# Second solution
class Solution:
    def countEven(self, num: int) -> int:
        """Counts the number of positive integers less than or equal to `num` whose digit sums are even.

        The digit sum of a positive integer is the sum of all its digits.

        Args:
            num (int): The upper bound integer.

        Returns:
            int: The count of positive integers ≤ num with an even digit sum.

        Example:
            >>> countEven(4)
            2
            >>> countEven(30)
            14

        Time complexity: O(log(num)), since summing the digits of num takes O(log(num)) time.
        Space complexity: O(log(num)), due to the space used to store the string representation of num.

        LeetCode: Beats 100% of submissions
        """
        return num // 2 if sum(map(int, str(num))) % 2 == 0 else (num - 1) // 2
