class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        Given two integer lists nums1 and nums2, return a list of their
        intersection. Each element in the result must appear as many times as
        it shows in both arrays and you may return the result in any order.

        :param list[int] nums1: list, containing integer values
        :param list[int] nums2: list, containing integer values
        :returns list[int] res: list, containing intersection of nums1 & nums2

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 98.58%
        """
        res = []
        i, j = 0, 0

        nums1.sort()
        nums2.sort()

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1

        return res
