class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        """
        Finds the maximum length of an alternating sublist in the given list.

        An alternating sublist is defined as a contiguous sublist of length at least 2 where:
            - The first two elements satisfy s[1] = s[0] + 1.
            - For each subsequent element s[i] (i >= 2), the difference with the previous element alternates between -1 and 1:
                s[2] - s[1] = -1,
                s[3] - s[2] = 1,
                s[4] - s[3] = -1,
                ..., up to s[m-1] - s[m-2] = (-1)**m.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            int: The length of the longest alternating sublist, or -1 if none exists.

        Example:
            >>> alternatingSubarray([2,3,2,3,2,1,2])
            5

        Time Complexity: O(n), where n is the length of the input list.
        Space Complexity: O(1)

        LeetCode: Beats 91.10% of submissions
        """
        longest = -1
        curr_len = 1
        expect = 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == expect:
                curr_len += 1
                expect *= -1
            elif nums[i] - nums[i - 1] == 1:
                curr_len = 2
                expect = -1
            else:
                curr_len = 1
                expect = 1

            if curr_len > 1:
                longest = max(longest, curr_len)

        return longest
