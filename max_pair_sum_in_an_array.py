class Solution:
    def maxSum(self, nums: list[int]) -> int:
        """
        Given an integer list nums, find the maximum sum of a pair of numbers such that
        the largest digit in both numbers is the same.

        For example, for the number 2373, the largest digit is 7.

        Returns:
            int: The maximum sum of such a pair, or -1 if no such pair exists.

        Example:
            >>> maxSum([51, 71, 17, 24])
            88

        Time Complexity: O(n * d), where n is the length of nums and d is the number of digits in the largest number.
        Space Complexity: O(k), where k is the number of possible largest digits (at most 10).

        LeetCode: Beats 98.38% of submissions
        """
        largest = {}
        max_ps = -1

        for num in nums:
            largest_d = max(str(num))

            if largest.get(largest_d, 0):
                if num + largest[largest_d] > max_ps:
                    max_ps = num + largest[largest_d]
                if num > largest[largest_d]:
                    largest[largest_d] = num
            else:
                largest[largest_d] = num

        return max_ps
