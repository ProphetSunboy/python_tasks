class Solution:
    def addedInteger(self, nums1: list[int], nums2: list[int]) -> int:
        """Finds the integer added to a list to transform it into another.

        Given two integer lists, `nums1` and `nums2`, of equal length.
        The list `nums2` is a permutation of the list `nums1` after
        adding some integer `x` to each of its elements. This function
        returns the integer `x`.

        Args:
            nums1 (list[int]): The original list.
            nums2 (list[int]): The transformed list.

        Returns:
            int: The integer `x` that was added to each element of `nums1`.

        Example:
            >>> addedInteger([2, 6, 4], [9, 7, 5])
            3
            >>> addedInteger([10], [5])
            -5

        LeetCode: Beats 100% of submissions.
        """
        return min(nums2) - min(nums1)
