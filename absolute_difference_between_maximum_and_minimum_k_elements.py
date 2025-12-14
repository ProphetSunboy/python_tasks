class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        """
        Given an integer list nums and an integer k, find the absolute difference
        between the sum of the k largest elements and the sum of the k smallest
        elements.

        Args:
            nums (List[int]): List of integers.
            k (int): Number of largest/smallest elements to consider.

        Returns:
            int: Absolute difference between the sum of the k largest and k
            smallest elements.

        Example:
            Input: nums = [2, 4, 7], k = 2
            Output: 5
            Explanation:
                Largest 2: [4, 7], sum = 11
                Smallest 2: [2, 4], sum = 6
                Absolute difference = 11 - 6 = 5

        Time Complexity: O(N log N) due to sorting.
        Space Complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        nums.sort()

        return sum(nums[-k:]) - sum(nums[:k])
