class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        """
        You are given a binary list nums (0-indexed).

        We define xi as the number whose binary representation is the subarray
        nums[0..i] (from most-significant-bit to least-significant-bit).

            For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.

        Return a list of booleans answer where answer[i] is True if xi is
        divisible by 5.

        :param list[int] nums: binary list
        :returns list[bool] answer: answer[i] is True if xi is divisible by 5

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 97.87%
        """
        res = []
        num = 0

        for n in nums:
            num = (num * 2 + n) % 5
            res.append(num == 0)

        return res
