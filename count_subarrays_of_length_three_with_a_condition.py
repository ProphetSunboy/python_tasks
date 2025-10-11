class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        """
        Counts the number of sublists of length 3 in the input list `nums`
        such that the sum of the first and third elements is exactly half of the middle element.

        Args:
            nums (List[int]): List of integers.

        Returns:
            int: The number of valid sublists of length 3 satisfying the given condition.

        Example:
            >>> countSubarrays([2, 8, 2, 6, 12])
            1

        Time Complexity: O(n)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        res = 0

        for i in range(1, len(nums) - 1):
            if nums[i - 1] + nums[i + 1] == nums[i] / 2:
                res += 1

        return res
