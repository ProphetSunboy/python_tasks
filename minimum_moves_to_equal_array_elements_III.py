class Solution:
    def minMoves(self, nums: List[int]) -> int:
        """
        Given an integer list nums, return the minimum total number of moves required
        so that all elements in nums become equal. In one move, you may increase the
        value of any single element nums[i] by 1.

        Args:
            nums (List[int]): List of integers.

        Returns:
            int: The minimum number of moves required to make all elements equal.

        Example:
            Input: nums = [1, 2, 3]
            Output: 3
            Explanation: Increment 1 twice and increment 2 once to reach [3, 3, 3].

        Time Complexity: O(n), where n is the length of the list.
        Space Complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        total_moves = 0
        max_val = max(nums)

        for i in range(len(nums)):
            total_moves += max_val - nums[i]

        return total_moves
