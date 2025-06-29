class Solution:
    def digit_sum(self, num: int) -> int:
        """Calculate the sum of all digits in a given number.

        This method iteratively extracts each digit from the number by taking
        the remainder when divided by 10 (num % 10) and then integer dividing
        by 10 to remove the last digit. This process continues until the
        number becomes 0.

        Args:
            num (int): The positive integer whose digits need to be summed.

        Returns:
            int: The sum of all digits in the input number.

        Example:
            >>> digit_sum(123)
            6
            >>> digit_sum(999)
            27
            >>> digit_sum(5)
            5
        """
        d_sum = 0

        while num > 0:
            d_sum += num % 10
            num //= 10

        return d_sum

    def countLargestGroup(self, n: int) -> int:
        """Count the number of groups with the largest size when grouping numbers by digit sum.

        Given an integer n, group the numbers from 1 to n according to the sum of their digits.
        Numbers with the same digit sum belong to the same group. For example, 14 and 5 both
        have digit sum 5, so they belong to the same group, while 13 (digit sum 4) and 3
        (digit sum 3) belong to different groups.

        Args:
            n (int): The upper bound for the range of numbers to group (1 to n).

        Returns:
            int: The number of groups that have the largest size.

        Example:
            >>> countLargestGroup(13)
            4
            >>> countLargestGroup(2)
            2

        LeetCode: Beats 94.88% of submissions
        """
        digits_d = [0] * 37

        for num in range(1, n + 1):
            d_sum = self.digit_sum(num)
            digits_d[d_sum] += 1

        return digits_d.count(max(digits_d))
