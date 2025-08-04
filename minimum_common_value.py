class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Given two integer lists nums1 and nums2, both sorted in non-decreasing order,
        return the minimum integer common to both lists. If there is no common integer, return -1.

        An integer is considered common if it appears in both lists.

        Args:
            nums1 (list[int]): First sorted list of integers.
            nums2 (list[int]): Second sorted list of integers.

        Returns:
            int: The smallest integer present in both lists, or -1 if no such integer exists.

        Example:
            >>> getCommon([1, 2, 3], [2, 4])
            2
            >>> getCommon([1, 3, 5], [2, 4, 6])
            -1

        Time complexity: O(n + m), where n and m are the lengths of nums1 and nums2.
        Space complexity: O(1).

        LeetCode: Beats 98.80% of submissions
        """
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                return nums1[i]

        return -1
