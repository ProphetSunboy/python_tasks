class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        """
        Computes the alternating sum of an integer list.

        The alternating sum of nums is defined as:
            nums[0] - nums[1] + nums[2] - nums[3] + ...
        that is, elements at even indices are added and those at odd indices are subtracted.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            int: The alternating sum of the list.

        Example:
            >>> alternatingSum([3, 1, 4, 2])
            4   # (3 - 1 + 4 - 2)
            >>> alternatingSum([10, 5, 3])
            8   # (10 - 5 + 3)

        Time Complexity: O(n), where n is the number of elements in nums.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        alt_sum = 0

        for i, num in enumerate(nums):
            if i % 2:
                alt_sum -= num
            else:
                alt_sum += num

        return alt_sum
