class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        """Finds the maximum absolute difference between adjacent elements in a circular list.

        In a circular list, the first and last elements are considered adjacent.

        Args:
            nums (list[int]): A list of integers representing the circular list

        Returns:
            int: The maximum absolute difference between any two adjacent elements

        Example:
            >>> maxAdjacentDistance([1, 2, 3, 4])
            3  # Maximum difference is between 4 and 1 (circular)

        Time complexity: O(n) - where n is length of nums
        Space complexity: O(1) - constant extra space used

        LeetCode: Beats 100% of submissions
        """
        max_diff = 0

        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[i] - nums[i - 1]) > max_diff:
                max_diff = abs(nums[i] - nums[i - 1])

        return max_diff
