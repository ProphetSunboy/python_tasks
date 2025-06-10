class Solution:
    def get_sum_of_digits(self, num: int) -> int:
        """Calculates the sum of all digits in a given number.

        Args:
            num (int): A positive integer to calculate digit sum for

        Returns:
            int: Sum of all digits in the number

        Example:
            >>> get_sum_of_digits(123)
            6  # 1 + 2 + 3 = 6

        Time complexity: O(log n) - where n is the input number
        Space complexity: O(1) - constant space used
        """
        s = 0

        while num > 0:
            s += num % 10
            num //= 10

        return s

    def differenceOfSum(self, nums: list[int]) -> int:
        """Calculates the absolute difference between element sum and digit sum of a list.

        The element sum is the sum of all elements in nums.
        The digit sum is the sum of all digits (not necessarily distinct) that appear in nums.

        Args:
            nums (list[int]): A list of positive integers

        Returns:
            int: The absolute difference between element sum and digit sum

        Example:
            >>> differenceOfSum([1, 15, 6, 3])
            9  # Element sum = 25, Digit sum = 16, Difference = |25 - 16| = 9

        Time complexity: O(n * log m) - where n is length of nums and m is max number
        Space complexity: O(1) - constant space used

        LeetCode: Beats 99.63% of submissions
        """
        elem_sum = sum(nums)
        digit_sum = 0

        for num in nums:
            digit_sum += self.get_sum_of_digits(num)

        return abs(elem_sum - digit_sum)
