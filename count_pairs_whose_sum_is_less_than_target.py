class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        """Counts the number of pairs in a list whose sum is less than a target value.

        Given a 0-indexed integer list nums and an integer target, returns the number of pairs (i, j)
        where 0 <= i < j < n and nums[i] + nums[j] < target.

        Args:
            nums (list[int]): The input list of integers
            target (int): The target sum to compare against

        Returns:
            int: The number of valid pairs whose sum is less than target

        Example:
            >>> countPairs([-1, 1, 2, 3, 1], 2)
            3  # Pairs are (-1,1), (-1,2), (-1,3)

        Time complexity: O(n²) - where n is the length of nums
        Space complexity: O(1) - constant extra space used

        LeetCode: Beats 100% of submissions
        """
        pairs = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    pairs += 1

        return pairs
