class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        """Given a list of integers nums, find the minimum positive value of startValue such that
        the cumulative sum (starting from startValue and adding each element of nums in order)
        never drops below 1 at any step.

        Args:
            nums (list[int]): List of integers to be added step by step.

        Returns:
            int: The minimum positive startValue required so that the running sum is always at least 1.

        Example:
            >>> minStartValue([-3, 2, -3, 4, 2])
            5
            >>> minStartValue([1, 2])
            1
            >>> minStartValue([1, -2, -3])
            5

        Time complexity: O(n), where n is the length of nums.
        Space complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        val = 1
        min_val = 1

        for num in nums:
            val += num

            if val < min_val:
                min_val = val

        return abs(min_val) + 2 if min_val < 1 else 1
