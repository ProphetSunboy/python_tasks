class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        """
        Given a list nums of integers, return how many of them contain an even
        number of digits.


        LeetCode Beats 100%
        """
        even = 0

        for num in nums:
            if len(str(num)) % 2 == 0:
                even += 1

        return even
