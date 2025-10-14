class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        Given an integer list nums, compute the minimum number of operations to
        make all elements equal using the following operation:

            - In one operation, choose any sublist nums[l...r] (0 <= l <= r < n)
            and replace every element in that sublist with the bitwise AND of all its elements.

        Returns:
            int: The minimum number of operations required to make all elements in nums equal.

        Example:
            >>> minOperations([1, 1, 1])
            0
            >>> minOperations([1, 3, 1])
            1

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(n)

        LeetCode: Beats 100% of submissions
        """
        if len(set(nums)) == 1:
            return 0

        return 1
