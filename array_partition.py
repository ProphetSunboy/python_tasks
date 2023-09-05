class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        """
        Given an integer array nums of 2n integers, group these integers into n
        pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi)
        for all i is maximized. Return the maximized sum.


        :param list[int] nums: list of 2n integers
        :returns int maximized_sum: maximized sum of the minimal elements among n groups

        Time complexity: O(nlogn)
        Space complexity: O(n)

        LeetCode: Beats 97.69%
        """
        nums.sort()
        return sum(nums[::2])
