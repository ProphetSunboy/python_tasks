class Solution:
    def longestAlternatingSubarray(self, nums: list[int], threshold: int) -> int:
        """
        You are given a 0-indexed integer array nums and an integer threshold.

        Find the length of the longest subarray of nums starting at index l and
        ending at index r (0 <= l <= r < nums.length) that satisfies the
        following conditions:

            nums[l] % 2 == 0
            For all indices i in the range [l, r - 1], nums[i] % 2 != nums[i + 1] % 2
            For all indices i in the range [l, r], nums[i] <= threshold

        Return an integer denoting the length of the longest such subarray.

        Note: A subarray is a contiguous non-empty sequence of elements within
        an array.

        :param list[int] nums: lict, containing integer numbers
        :param int threshold: subarray element limit
        :returns int len_longest_subarray: the length of the longest subarray matching the conditions

        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 99.52%
        """
        longest = 0
        curr = 0

        for i, num in enumerate(nums):
            if curr == 0:
                if num % 2 == 0 and num <= threshold:
                    curr = 1
            else:
                curr += 1

                if num > threshold or (curr != 0 and num % 2 == nums[i - 1] % 2):
                    if curr - 1 > longest:
                        longest = curr - 1

                    curr = 0

                    if num % 2 == 0 and num <= threshold:
                        curr = 1

        return max(curr, longest)
