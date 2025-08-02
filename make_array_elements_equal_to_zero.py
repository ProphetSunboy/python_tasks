class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        """
        Given an integer list nums, determine the number of valid ways to select
        a starting position and movement direction such that all elements of nums
        become zero by following a specific process.

        Process:
            1. Choose a starting index curr where nums[curr] == 0, and pick a movement direction (left or right).
            2. Repeat the following steps:
                - If curr is out of bounds ([0, n-1]), stop.
                - If nums[curr] == 0, move one step in the current direction (increment curr for right, decrement for left).
                - If nums[curr] > 0:
                    - Decrement nums[curr] by 1.
                    - Reverse the movement direction.
                    - Move one step in the new direction.
            3. The selection is valid if, after the process, all elements in nums are zero.

        Args:
            nums (list[int]): The input list of integers.

        Returns:
            int: The number of valid (starting position, direction) pairs.

        Example:
            >>> countValidSelections([1,0,2,0,3])
            2

        Time complexity: O(n), where n is the length of nums.
        Space complexity: O(1).

        LeetCode: Beats 97.45% of submissions
        """
        l_sum, r_sum = 0, sum(nums)
        valid = 0

        for num in nums:
            if num == 0:
                if l_sum == r_sum:
                    valid += 2
                elif abs(l_sum - r_sum) == 1:
                    valid += 1
            else:
                l_sum += num
                r_sum -= num

        return valid
