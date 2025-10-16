class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        """
        Given a positive integer list nums and an integer k, select at most k distinct
        elements from nums such that their sum is maximized.

        The returned list should contain the chosen numbers in strictly descending order.

        Args:
            nums (List[int]): The input list of positive integers.
            k (int): The maximum number of elements to choose.

        Returns:
            List[int]: List of at most k distinct elements from nums with the largest
            values, in strictly descending order.

        Example:
            >>> maxKDistinct([3, 1, 4, 2], 2)
            [4, 3]
            >>> maxKDistinct([5, 3, 5, 3, 1], 3)
            [5, 3, 1]

        Time Complexity: O(n log n), where n is the length of nums (for sorting and deduplication).
        Space Complexity: O(n) (to store unique elements).

        LeetCode: Beats 100% of submissions
        """
        return sorted(set(nums), reverse=True)[:k]
