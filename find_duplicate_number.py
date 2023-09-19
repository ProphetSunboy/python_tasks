class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        """
        Given a list of integers nums containing n + 1 integers where each
        integer is in the range [1, n] inclusive.

        There is only one repeated number in nums, return this repeated number.

        :param list[int] nums: list of integers
        :returns int repeated_num: repeated number in nums

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 94.70%
        """
        c = {}

        for num in nums:
            c[num] = c.get(num, 0) + 1

            if c[num] > 1:
                return num
