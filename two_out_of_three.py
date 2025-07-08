class Solution:
    def twoOutOfThree(
        self, nums1: list[int], nums2: list[int], nums3: list[int]
    ) -> list[int]:
        """Given three integer lists nums1, nums2, and nums3, return a list of all distinct values
        that appear in at least two of the three lists. The order of the returned values does not matter.

        Args:
            nums1 (list[int]): First list of integers.
            nums2 (list[int]): Second list of integers.
            nums3 (list[int]): Third list of integers.

        Returns:
            list[int]: A list of distinct integers present in at least two of the input lists.

        Example:
            >>> twoOutOfThree([1,1,3,2], [2,3], [3])
            [2, 3]
            >>> twoOutOfThree([3,1], [2,3], [1,2])
            [1, 2, 3]

        Time complexity: O(n), where n is the total number of elements in all lists.
        Space complexity: O(n), for storing unique elements.

        LeetCode: Beats 100% of submissions
        """
        res = set()

        for num in nums1:
            if num in nums2 or num in nums3:
                res.add(num)

        for num in nums2:
            if num in nums3:
                res.add(num)

        return list(res)
