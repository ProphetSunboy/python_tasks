class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        """
        You are given an integer array nums and an integer k.

        In one operation, you can choose any index i where 0 <= i < nums.length
        and change nums[i] to nums[i] + x where x is an integer from the range
        [-k, k]. You can apply this operation at most once for each index i.

        The score of nums is the difference between the maximum and minimum
        elements in nums.

        Return the minimum score of nums after applying the mentioned operation
        at most once for each index in it.

        :param list[int] nums: list of integers
        :returns int good_pairs: number of good pairs in nums

        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 99.36%
        """
        max_el = max(nums)
        min_el = min(nums)

        return max(0, max_el - k - min_el - k)
