class Solution:
    def isTrionic(self, nums: list[int]) -> bool:
        """
        Determines if the given integer list nums is trionic.

        A list is trionic if there exist indices 0 < p < q < n-1 such that:
            - nums[0...p] is strictly increasing,
            - nums[p...q] is strictly decreasing,
            - nums[q...n-1] is strictly increasing.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            bool: True if nums is trionic, False otherwise.

        Example:
            >>> isTrionic([1, 3, 2, 4, 5])
            True
            >>> isTrionic([1, 2, 3, 2, 1])
            False

        Time Complexity: O(N), where N is the length of nums.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        i = 1
        j = 1

        while i < len(nums) and nums[i] > nums[i - 1]:
            i += 1

        if i == j or i == len(nums) - 1:
            return False

        j = i
        while i < len(nums) and nums[i] < nums[i - 1]:
            i += 1

        if i == j or i == len(nums):
            return False

        while i < len(nums) and nums[i] > nums[i - 1]:
            i += 1

        return i == len(nums)
