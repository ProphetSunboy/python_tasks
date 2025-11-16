class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        """
        Given an integer list nums, pick three distinct elements a, b, and c (at different indices)
        such that the value of the expression (a + b - c) is maximized.

        Args:
            nums (List[int]): The list of integers.

        Returns:
            int: The maximum possible value of a + b - c for any three distinct indices.

        Example:
            Input:  nums = [1, 2, 3, 4]
            Output: 6

        Time Complexity: O(n log n), where n is the length of nums (due to sorting).
        Space Complexity: O(1), ignoring input and output.

        LeetCode: Beats 100% of submissions
        """
        nums.sort()

        return nums[-1] + nums[-2] - nums[0]
