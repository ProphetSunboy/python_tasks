class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        """
        Given a list nums of even length n, pair up the elements of nums into n / 2 pairs
        such that each element is in exactly one pair and the maximum pair sum (a + b for a pair)
        is minimized.

        The pair sum of a pair (a, b) is a + b. The maximum pair sum is the largest across all pairs.
        For example, for the pairs (1, 5), (2, 3), and (4, 4), the maximum pair sum is
        max(1 + 5, 2 + 3, 4 + 4) = max(6, 5, 8) = 8.

        This function returns the minimized maximum pair sum after optimally
        pairing up the elements.

        Args:
            nums (List[int]): List of integers of even length.

        Returns:
            int: The minimized maximum pair sum.

        Example:
            Input: nums = [3, 5, 2, 3]
            Output: 7

        Time Complexity: O(n log n), where n is the number of elements in nums.
        Space Complexity: O(1)
        """
        nums.sort()

        i = 0
        max_psum = 0
        while i < len(nums) // 2:
            if nums[i] + nums[len(nums) - i - 1] > max_psum:
                max_psum = nums[i] + nums[len(nums) - i - 1]

            i += 1

        return max_psum
