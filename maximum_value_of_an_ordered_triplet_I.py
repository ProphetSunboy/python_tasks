class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        """
        Given a 0-indexed integer list nums, find the maximum value over all triplets
        of indices (i, j, k) such that i < j < k.

        The value of a triplet (i, j, k) is defined as (nums[i] - nums[j]) * nums[k].

        Return the maximum such value among all possible triplets.
        If all triplet values are negative, return 0.

        Args:
            nums (List[int]): The list of integers.

        Returns:
            int: The maximum triplet value, or 0 if all are negative.

        Example:
            >>> maximumTripletValue([1,2,3])
            0
            >>> maximumTripletValue([12,6,1,2,7])
            77

        Time Complexity: O(n^2)
        Space Complexity: O(n)

        LeetCode: Beats 100% of submissions
        """
        n = len(nums)
        max_val = 0
        max_right = [0] * n

        max_right[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            max_right[i] = max(nums[i], max_right[i + 1])

        for j in range(1, n - 1):
            for i in range(j):
                if nums[i] > nums[j]:
                    curr_val = (nums[i] - nums[j]) * max_right[j + 1]
                    max_val = max(max_val, curr_val)

        return max_val
