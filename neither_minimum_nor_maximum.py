class Solution:
    def findNonMinOrMax(self, nums: list[int]) -> int:
        """Given an integer list nums containing distinct positive integers, return
        any number from the list that is neither the minimum nor the maximum value
        in the list. If no such number exists (i.e., the list has fewer than 3 elements), return -1.

        Args:
            nums (List[int]): List of distinct positive integers.

        Returns:
            int: An integer from nums that is neither the minimum nor the maximum, or -1 if not possible.

        Example:
            >>> findNonMinOrMax([3, 1, 2])
            2

        Time complexity: O(n log n)
        Space complexity: O(n)

        LeetCode: Beats 94.24% of submissions
        """
        if len(nums) < 3:
            return -1

        return sorted(nums)[1]
