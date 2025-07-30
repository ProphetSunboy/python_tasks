class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        """Given an integer list nums, find the length of the longest non-empty sublist
        whose bitwise AND is equal to the maximum possible bitwise AND of any sublist in nums.

        The bitwise AND of a sublist is the result of applying the bitwise AND operation to all its elements.
        A sublist is a contiguous sequence of elements within the list.

        Args:
            nums: List of non-negative integers.

        Returns:
            int: The length of the longest sublist with the maximum possible bitwise AND.

        Example:
            >>> longestSubarray([1,2,3,3,2,2])
            2  # The maximum AND is 3, and the longest sublist with AND 3 has length 2.

        Time complexity: O(n), where n is the length of nums.
        Space complexity: O(1).

        LeetCode: Beats 90.53% of submissions
        """
        max_and = max(nums)
        longest = 0

        curr = 0
        for i in range(len(nums)):
            if nums[i] == max_and:
                curr += 1
            else:
                if curr > longest:
                    longest = curr

                curr = 0

        if curr > longest:
            longest = curr

        return longest
