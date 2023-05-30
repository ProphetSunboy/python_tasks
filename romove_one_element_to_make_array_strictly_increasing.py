class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        """
        Given a 0-indexed integer array nums, return true if it can be made
        strictly increasing after removing exactly one element, or false
        otherwise. If the array is already strictly increasing, return true.
        """
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                break
        nums_1 = nums[:i] + nums[i+1:]
        nums_2 = nums[:i+1] + nums[i+2:]
        return nums_1 == sorted(set(nums_1)) or nums_2 == sorted(set(nums_2))