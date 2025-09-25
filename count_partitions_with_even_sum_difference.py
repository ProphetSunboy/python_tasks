class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        """
        Given an integer lsit nums of length n, count the number of valid partitions.

        A partition is defined as an index i where 0 <= i < n - 1, splitting the list into two non-empty sublists:
            - Left sublist: nums[0..i]
            - Right sublist: nums[i+1..n-1]

        A partition is valid if the difference between the sum of the left and right sublists is even.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            int: The number of partitions where the difference between the left and right sublist sums is even.

        Example:
            >>> countPartitions([1, 2, 3, 4])
            3

        Time Complexity: O(N), where N is the length of nums.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        even_partitions = 0
        l, r = 0, sum(nums)

        for i in range(len(nums) - 1):
            l += nums[i]
            r -= nums[i]

            if (l - r) % 2 == 0:
                even_partitions += 1

        return even_partitions
