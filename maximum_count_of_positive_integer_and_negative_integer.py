class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        """
        Given a sorted list nums (in non-decreasing order), return the maximum count
        between positive and negative integers in the list.

        0 is considered neither positive nor negative.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            int: The maximum of the count of positive and negative integers.

        Example:
            >>> maximumCount([-2, -1, 0, 1, 2, 3])
            3

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        pos, neg = 0, 0

        for num in nums:
            if num > 0:
                pos += 1
            elif num < 0:
                neg += 1

        return max(pos, neg)
