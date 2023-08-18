class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        """
        Given a binary list nums, return the maximum number of consecutive 1's
        in the list.

        :param list[int] nums: binary list
        :returns int max_cons: maximum number of consecutive 1's

        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 99.73%
        """
        max_cons = 0
        curr = 0

        for num in nums:
            if num == 1:
                curr += 1
            else:
                if curr > max_cons:
                    max_cons = curr

                curr = 0

        if curr > max_cons:
            max_cons = curr

        return max_cons
