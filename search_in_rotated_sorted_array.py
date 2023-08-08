class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Given the list nums after the possible rotation and an integer target,
        return the index of target if it is in nums, or -1 if it is not in nums.

        There is an integer list nums sorted in ascending order (with distinct
        values).

        Prior to being passed to function, nums is possibly rotated at an
        unknown pivot index k (1 <= k < nums.length) such that the resulting
        array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ...,
        nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at
        pivot index 3 and become [4,5,6,7,0,1,2].

        :param list[int] matrix: list of integer numbers
        :param int target: number to be found
        :returns int i: index of target if it is in nums, otherwise -1

        Time complexity: O(n)
        Space complexity: O(1)


        LeetCode: Beats 92.77%
        """
        return nums.index(target) if target in nums else -1
