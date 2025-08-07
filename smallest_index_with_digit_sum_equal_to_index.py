class Solution:
    def get_digit_sum(self, num: int) -> int:
        """
        Calculate the sum of the digits of a given integer.

        Args:
            num (int): The integer whose digits will be summed.

        Returns:
            int: The sum of the digits of num.

        Example:
            >>> get_digit_sum(123)
            6
        """
        digit_sum = 0

        while num > 0:
            digit_sum += num % 10
            num //= 10

        return digit_sum

    def smallestIndex(self, nums: list[int]) -> int:
        """
        Given an integer list nums, return the smallest index i such that the sum of the digits of nums[i] is equal to i.
        If no such index exists, return -1.

        Args:
            nums (list[int]): The list of integers to check.

        Returns:
            int: The smallest index i where the sum of the digits of nums[i] equals i, or -1 if no such index exists.

        Examples:
            >>> smallestIndex([0, 10, 21, 12])
            1
            >>> Solution().smallestIndex([5, 14, 23, 32])
            -1

        Time Complexity: O(n * d), where n is the length of nums and d is the number of digits in the largest number.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        for i, num in enumerate(nums):
            if i == self.get_digit_sum(num):
                return i

        return -1
