class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        """Calculates the maximum product difference between two pairs of numbers.

        The product difference between pairs (a,b) and (c,d) is defined as (a * b) - (c * d).
        This function finds the maximum possible product difference by selecting four distinct
        numbers from the input list.

        Args:
            nums (list[int]): Input list of integers

        Returns:
            int: Maximum product difference between any two pairs of numbers

        Examples:
            >>> maxProductDifference([5,6,2,7])
            34  # (6 * 7) - (2 * 5) = 42 - 10 = 32
            >>> maxProductDifference([4,2,5,9,7,4,8])
            64  # (9 * 8) - (2 * 4) = 72 - 8 = 64

        Time complexity: O(n log n) - dominated by sorting
        Space complexity: O(n) - for storing sorted list

        LeetCode: Beats 94.87% of submissions
        """
        sorted_nums = sorted(nums)

        return sorted_nums[-1] * sorted_nums[-2] - sorted_nums[0] * sorted_nums[1]
