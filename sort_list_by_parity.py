class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        """
        Given an integer list nums, move all the even integers at the beginning
        of the list followed by all the odd integers.

        Return any list that satisfies this condition.

        :param list[int] nums: integer list
        :returns list[int] parity: all the even integers of nums are moved at
        the beginning of the list followed by all the odd integers.

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 96.82%
        """
        evens = []
        odds = []

        for num in nums:
            if num % 2:
                odds.append(num)
            else:
                evens.append(num)

        return evens + odds


class SecondSolution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        """
        :param list[int] nums: integer list
        :returns list[int] parity: all the even integers of nums are moved at
        the beginning of the list followed by all the odd integers.

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 90.99%
        """
        i = 0
        parity = [0] * len(nums)

        for num in nums:
            if num % 2 == 0:
                parity[i] = num
                i += 1

        for num in nums:
            if num % 2:
                parity[i] = num
                i += 1

        return parity
