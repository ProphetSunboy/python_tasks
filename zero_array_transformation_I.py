# First Solution
class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        """
        You are given an integer list nums of length n and a 2D list queries,
        where queries[i] = [li, ri].

        For each queries[i]:

        Select a subset of indices within the range [li, ri] in nums.
        Decrement the values at the selected indices by 1.
        A Zero List is a list where all elements are equal to 0.

        Return True if it is possible to transform nums into a Zero List after
        processing all the queries sequentially, otherwise return False.
        """
        sub = [0] * len(nums)

        for querie in queries:
            for i in range(querie[0], querie[1] + 1):
                sub[i] += 1

        for i in range(len(nums)):
            if (nums[i] - sub[i]) > 0:
                return False

        return True
