class Solution:
    def validMountainArray(self, nums: list[int]) -> bool:
        """
        Given a list of integers nums, return True if and only if it is a valid
        mountain list.

        Recall that nums is a mountain list if and only if:

            nums.length >= 3
            There exists some i with 0 < i < nums.length - 1 such that:
                nums[0] < nums[1] < ... < nums[i - 1] < nums[i]
                nums[i] > nums[i + 1] > ... > nums[nums.length - 1]

        :param list[int] nums: list of integers
        :returns bool is_mountain: nums is a valid mountain list

        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 99.80%
        """
        if len(nums) < 3:
            return False

        peak = False

        for i in range(1, len(nums)):
            if not peak:
                if nums[i] <= nums[i - 1]:
                    peak = True
                    if i == 1 or nums[i] == nums[i - 1]:
                        return False
            else:
                if nums[i] >= nums[i - 1]:
                    return False

        return peak
