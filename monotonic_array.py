class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        """
        An array is monotonic if it is either monotone increasing or monotone
        decreasing.

        An array nums is monotone increasing if for all i <= j,
        nums[i] <= nums[j].An array nums is monotone decreasing if
        for all i <= j, nums[i] >= nums[j].

        Given an integer array nums, return true if the given
        array is monotonic, or False otherwise.

        LeetCode: Beats 92.51%
        """
        prev = 0
        i = 1

        while i < len(nums) and prev == 0:
            curr = nums[i] - nums[i - 1]

            if curr != 0:
                prev = 1 if curr > 0 else -1

            i += 1

        for j in range(i, len(nums)):
            curr = nums[j] - nums[j - 1]

            if curr * prev < 0:
                return False

        return True
