class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        """Returns the maximum possible sum of a strictly increasing sublist in
        the given list of positive integers.

        A sublist is a contiguous sequence of elements within the list. A strictly
        increasing sublist is one where each element is greater than the previous one.

        Args:
            nums (list[int]): The input list of positive integers.

        Returns:
            int: The maximum sum of any strictly increasing sublist in nums.

        Example:
            >>> maxAscendingSum([10, 20, 30, 5, 10, 50])
            65  # The subarray [5, 10, 50] has the maximum sum

        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        max_asc = 0
        curr = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr += nums[i]
            else:
                if curr > max_asc:
                    max_asc = curr
                curr = nums[i]

        if curr > max_asc:
            max_asc = curr

        return max_asc
