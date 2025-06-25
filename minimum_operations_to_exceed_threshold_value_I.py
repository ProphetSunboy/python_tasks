class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        """Calculates the minimum operations to make all list elements >= k.

        In one operation, you can remove the smallest element from `nums`. This
        function finds the minimum number of operations so that all remaining
        elements are greater than or equal to `k`.

        Args:
            nums (list[int]): The input integer list.
            k (int): The threshold value.

        Returns:
            int: The minimum number of operations required.

        Example:
            >>> minOperations(nums=[2, 11, 10, 1, 3], k=10)
            3
            >>> minOperations(nums=[1, 1, 2, 4, 9], k=9)
            4

        LeetCode: Beats 100% of submissions
        """
        sorted_nums = sorted(nums)
        operations_count = 0

        for i in range(len(sorted_nums)):
            if sorted_nums[i] >= k:
                operations_count = i
                break

        return operations_count
