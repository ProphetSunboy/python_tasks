class Solution:
    def get_digit_sum(self, num: int) -> int:
        """
        Calculates the sum of the digits of a given integer.

        Args:
            num (int): The input integer whose digits will be summed.

        Returns:
            int: The sum of the digits of the input integer.

        Example:
            >>> get_digit_sum(123)
            6
            >>> get_digit_sum(405)
            9
        """
        digit_sum = 0

        while num > 0:
            digit_sum += num % 10
            num //= 10

        return digit_sum

    def minElement(self, nums: list[int]) -> int:
        """Replaces each element in the input list with the sum of its digits,
        then returns the minimum value among the replaced elements.

        Args:
            nums (list[int]): The input list of integers.

        Returns:
            int: The minimum digit sum among all elements after replacement.

        Example:
            >>> minElement([2, 11, 10, 1, 3])
            1
            >>> minElement([123, 456, 789])
            6

        LeetCode: Beats 100% of submissions
        """
        min_digit_sum = nums[0]

        for num in nums:
            n = self.get_digit_sum(num)

            if n < min_digit_sum:
                min_digit_sum = n

        return min_digit_sum
