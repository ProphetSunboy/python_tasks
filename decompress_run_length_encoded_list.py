class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        """Decompresses a run-length encoded list.

        Given a list `nums` of integers representing a list compressed
        with run-length encoding.

        Consider each adjacent pair of elements `[freq, val] = [nums[2*i], nums[2*i+1]]`
        (with `i >= 0`). For each such pair, there are `freq` elements with
        value `val`. This function concatenates all the sublists from left to
        right to generate the decompressed list.

        Args:
            nums (list[int]): The run-length encoded list.

        Returns:
            list[int]: The decompressed list.

        Example:
            Input: nums = [1, 2, 3, 4]
            Output: [2, 4, 4, 4]
            Explanation: The first pair [1,2] means we have 1 element with
                         value 2; the second pair [3,4] means we have 3
                         elements with value 4. The final list is
                         [2] + [4,4,4] = [2,4,4,4].

        Time complexity: O(N), where N is the length of the output list.
        Space complexity: O(N), to store the output list.

        LeetCode: Beats 100% of submissions
        """
        res = []

        for i in range(0, len(nums), 2):
            res += [nums[i + 1]] * nums[i]

        return res
