class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        """
        Given an integer list nums, return True if the given array is
        monotonic, or False otherwise.

        An array is monotonic if it is either monotone increasing or monotone
        decreasing.

        An array nums is monotone increasing if for all i <= j,
        nums[i] <= nums[j]. An array nums is monotone decreasing if for all
        i <= j, nums[i] >= nums[j].

        :param list[int] nums: integer list
        :returns bool is_monotonic: nums is either monotone increasing or
        monotone decreasing

        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 95.72%
        """
        mono_inc = True
        mono_dec = True

        i = 1
        k = 1
        for i in range(k, len(nums)):
            if nums[i] - nums[i - 1] < 0:
                mono_inc = False
                break

            if nums[i] - nums[i - 1] > 0:
                mono_dec = False
                break

        k = i

        for i in range(k, len(nums)):
            if nums[i] - nums[i - 1] < 0:
                mono_inc = False
                break

        if mono_inc:
            return True

        k = i

        for i in range(k, len(nums)):
            if nums[i] - nums[i - 1] > 0:
                mono_dec = False
                break

        return mono_dec
