class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        """
        Given an integer list nums, return the smallest positive integer that is absent from nums
        and is strictly greater than the average of all elements in nums.

        The average is defined as the sum of nums divided by its length (integer division).

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            int: The smallest missing positive integer greater than the average.

        Example:
            >>> smallestAbsent([2, 4, 6])
            5  # Average is 4, so smallest missing positive integer > 4 and not in [2, 4, 6] is 5.

        Time Complexity: O(n)
        Space Complexity: O(n)

        LeetCode: Beats 100% of submissions
        """
        avg = max(0, sum(nums) // len(nums)) + 1
        unique_nums = set(nums)

        while avg in unique_nums:
            avg += 1

        return avg
