class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        """
        Given two 0-indexed integer lists nums1 and nums2, return a list answer
        of size 2 where:

            answer[0] is a list of all distinct integers in nums1 which are not
            present in nums2.
            answer[1] is a list of all distinct integers in nums2 which are not
            present in nums1.

        Note that the integers in the lists may be returned in any order.

        :param list[int] nums1: integer list
        :param list[int] nums2: integer list
        :returns list[list[int]] answer: consist of unique items for each list

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 99.59%
        """
        a = set(nums1)
        b = set(nums2)

        return [a - b, b - a]
