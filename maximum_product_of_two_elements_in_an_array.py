class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        """Find the maximum product of (nums[i]-1)*(nums[j]-1) for any two different indices i and j in the list.

        Args:
            nums (list[int]): List of integers

        Returns:
            int: Maximum value of (nums[i]-1)*(nums[j]-1)

        Example:
            >>> maxProduct([3,4,5,2])
            12  # (5-1)*(4-1) = 4*3 = 12

        Time complexity: O(n) - single pass through list to find two largest numbers
        Space complexity: O(1) - constant space using two variables

        LeetCode: Beats 100% of submissions
        """
        max1 = 0
        max2 = 0

        for num in nums:
            if num > max1:
                max1, max2 = num, max1
            elif num > max2:
                max2 = num

        return (max1 - 1) * (max2 - 1)
