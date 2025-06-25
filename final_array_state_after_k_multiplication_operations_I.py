class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        """Given an integer list nums, an integer k, and an integer multiplier, perform k operations on nums.
        In each operation, find the minimum value in nums (choosing the first occurrence if there are duplicates),
        and replace it with its value multiplied by multiplier.

        Args:
            nums (list[int]): The input list of integers.
            k (int): The number of operations to perform.
            multiplier (int): The value to multiply the selected minimum by.

        Returns:
            list[int]: The final state of nums after performing all k operations.

        Example:
            >>> getFinalState([2, 11, 10, 1, 3], 2, 3)
            [6, 11, 10, 3, 3]

        LeetCode: Beats 100% of submissions
        """
        for _ in range(k):
            nums[nums.index(min(nums))] *= multiplier

        return nums
