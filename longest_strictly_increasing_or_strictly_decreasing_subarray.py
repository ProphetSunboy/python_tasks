class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        """
        Returns the length of the longest contiguous sublist in nums that is either strictly increasing or strictly decreasing.

        A sublist is a contiguous, non-empty sequence of elements within the list.

        Args:
            nums (list[int]): List of integers.

        Returns:
            int: The length of the longest strictly increasing or strictly decreasing sublist.

        Example:
            >>> longestMonotonicSubarray([1, 2, 3, 2, 1, 0])
            4

        Time Complexity: O(n)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        longest = 1
        curr = 1
        inc = True

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                if inc:
                    curr += 1
                else:
                    if curr > longest:
                        longest = curr

                    curr = 2
                    inc = True
            elif nums[i] < nums[i - 1]:
                if inc:
                    if curr > longest:
                        longest = curr

                    curr = 2
                    inc = False
                else:
                    curr += 1
            else:
                if curr > longest:
                    longest = curr

                curr = 1

        if curr > longest:
            longest = curr

        return longest
