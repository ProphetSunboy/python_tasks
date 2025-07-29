class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        """Given a non-negative integer list nums, return the minimum number of
        operations required to make every element in nums equal to 0.

        In one operation:
            - Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
            - Subtract x from every positive element in nums.

        Args:
            nums (list[int]): The input list of non-negative integers.

        Returns:
            int: The minimum number of operations to make all elements zero.

        Example:
            >>> minimumOperations([1, 5, 0, 3, 5])
            3

        Time complexity: O(n), where n is the length of nums (due to set and sort operations).
        Space complexity: O(n), for storing unique elements.

        LeetCode: Beats 100% of submissions
        """
        n = sorted(set(nums))
        curr = n[0]
        ops = 0
        i = 1

        if n[0] > 0:
            ops += 1

        while i < len(n):
            if n[i] > n[i - 1] or n[i] == 0:
                nums[i] -= curr
                curr += nums[i]
                nums[i] = 0
                ops += 1
            i += 1

        return ops
