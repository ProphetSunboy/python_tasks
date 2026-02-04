class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        """
        Given an integer list nums of length n, find the maximum sum of any
        trionic sublist.

        A trionic sublist is a contiguous sublist nums[l...r] (with 0 <= l < r < n)
        for which there exist indices l < p < q < r such that:
            - nums[l...p] is strictly increasing,
            - nums[p...q] is strictly decreasing,
            - nums[q...r] is strictly increasing.

        Args:
            nums (List[int]): The list of integers.

        Returns:
            int: The maximum sum of any trionic sublist in nums.

        Example:
            Input: nums = [1,4,2,7]
            Output: 14

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(n), for storing DP lists.

        LeetCode: Beats 97.81% of submissions
        """
        n = len(nums)
        if n < 4:
            return -1

        f1 = [float("-inf")] * n
        f2 = [float("-inf")] * n
        f3 = [float("-inf")] * n

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                f1[i] = max(f1[i - 1] + nums[i], nums[i - 1] + nums[i])

            if nums[i] < nums[i - 1]:
                f2[i] = max(f1[i - 1] + nums[i], f2[i - 1] + nums[i])

            if nums[i] > nums[i - 1]:
                f3[i] = max(f2[i - 1] + nums[i], f3[i - 1] + nums[i])

        ans = max(f3)
        return int(ans) if ans > float("-inf") else -1
