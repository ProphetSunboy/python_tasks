class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Given an integer array nums, move all 0's to the end of it while
        maintaining the relative order of the non-zero elements.

        Note that you must do this in-place without making a copy of the array.
        """
        j = 0
        count_zero = 0

        for i, num in enumerate(nums):
            if num != 0:
                nums[j] = num
                j += 1
            else:
                count_zero += 1
                
        while count_zero > 0 and i >= 0:
            nums[i] = 0
            count_zero -= 1
            i -= 1