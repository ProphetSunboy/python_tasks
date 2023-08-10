class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        """
        Given the array nums after the rotation and an integer target,
        return True if target is in nums, or False if it is not in nums.

        There is an integer list nums sorted in non-decreasing order (not
        necessarily with distinct values).

        Before being passed to function, nums is rotated at an unknown
        pivot index k (0 <= k < nums.length) such that the resulting array is
        [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
        (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at
        pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

        :param list[int] nums: list of integer numbers
        :param int target: search value
        :returns bool ans: search result

        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 97.39%
        """
        for i in range(len(nums)):
            if i < len(nums) - 1 and nums[i] > nums[i + 1] and target > nums[i]:
                return False
            elif nums[i] == target:
                return True

        return False
