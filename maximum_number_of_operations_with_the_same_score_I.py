class Solution:
    def maxOperations(self, nums: list[int]) -> int:
        """
        Given a list of integers nums, you can repeatedly perform the following operation:
            - Delete the first two elements of nums and define the score of the operation as the sum of these two elements.
            - You can perform this operation as long as nums contains at least two elements.
            - All operations must yield the same score.

        Returns the maximum number of operations you can perform under these constraints.

        Args:
            nums (list[int]): The input list of integers.

        Returns:
            int: The maximum number of operations with the same score.

        Example:
            >>> maxOperations([3,2,1,4,5])
            2
            >>> maxOperations([1,1,1,1,1,1])
            3

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        ops = 0
        i = 0

        score = nums[0] + nums[1]
        while i < len(nums) - 1:
            curr_score = nums[i] + nums[i + 1]

            if curr_score != score:
                break

            ops += 1
            i += 2

        return ops
