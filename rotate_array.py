class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Given an integer array nums, rotate the array to the right by k steps,
        where k is non-negative.
        """
        temp = []
        k= k % len(nums)
        temp = nums[-k:]
        nums[k:] = nums[:-k]
        nums[:k] = temp