class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        Given an integer array nums (0-indexed). In one operation, you can
        choose an element of the array and increment it by 1.

        For example, if nums = [1,2,3], you can choose to increment nums[1] to
        make nums = [1,3,3].

        Return the minimum number of operations needed to make nums strictly
        increasing.
        """
        next_num = 0
        operations = 0
        for i in range(len(nums)-1):
            if next_num != 0:
                if next_num >= nums[i+1]:
                    operations += next_num + 1 - nums[i+1]
                    next_num += 1
                else:
                    next_num = 0
            else:
                if nums[i] >= nums[i+1]:
                    operations += nums[i] + 1 - nums[i+1]
                    next_num = nums[i] + 1
                else:
                    next_num = 0
        return operations