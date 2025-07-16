class Solution:
    def smallestEqual(self, nums: list[int]) -> int:
        """Returns the smallest index i in the 0-indexed integer list nums such that i % 10 == nums[i].
        If no such index exists, returns -1.

        Args:
            nums (list[int]): The input list of integers.

        Returns:
            int: The smallest index satisfying the condition, or -1 if none exists.

        Example:
            >>> smallestEqual([0,1,2])
            0
            >>> smallestEqual([4,3,2,1])
            2

        Time complexity: O(n), where n is the length of nums.
        Space complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        for i, num in enumerate(nums):
            if i % 10 == num:
                return i

        return -1
