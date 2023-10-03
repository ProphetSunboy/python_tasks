class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        """
        Given a list of integers nums, return the number of good pairs.

        A pair (i, j) is called good if nums[i] == nums[j] and i < j.

        :param list[int] nums: list of integers
        :returns int good_pairs: number of good pairs in nums

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 97.85%
        """
        good_pairs = 0
        count = collections.Counter(nums)

        for val in count.values():
            good_pairs += ((val - 1) * val) // 2

        return good_pairs
