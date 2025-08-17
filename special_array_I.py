class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        """
        Determines if a list is "special", meaning every pair of adjacent elements has different parity
        (i.e., one is even and the other is odd).

        Args:
            nums (list[int]): The input list of integers.

        Returns:
            bool: True if nums is a special list, False otherwise.

        Example:
            >>> =isArraySpecial([1, 2, 3, 4])
            True
            >>> isArraySpecial([2, 4, 6])
            False

        Time Complexity: O(n)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i - 1] % 2:
                return False

        return True
