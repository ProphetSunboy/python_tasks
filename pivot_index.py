class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        """
        Given an array of integers nums, calculate the pivot index of this array.

        The pivot index is the index where the sum of all the numbers strictly
        to the left of the index is equal to the sum of all the numbers strictly
        to the index's right.

        If the index is on the left edge of the array, then the left sum is 0
        because there are no elements to the left. This also applies to the
        right edge of the array.

        Return the leftmost pivot index. If no such index exists, return -1.

        :param list[int] nums: list of integers
        :returns int pivot: pivot index if it exists, -1 otherwise

        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 99.97%
        """
        l, r = 0, sum(nums)

        for i, num in enumerate(nums):
            r -= num

            if l == r:
                return i

            l += num

        return -1
