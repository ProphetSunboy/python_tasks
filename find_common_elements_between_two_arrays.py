class Solution:
    def findIntersectionValues(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """Finds the number of elements from each list that exist in the other list.

        Given two integer lists nums1 and nums2, calculates:
        1. The count of elements in nums1 that exist in nums2
        2. The count of elements in nums2 that exist in nums1

        Args:
            nums1 (list[int]): First list of integers
            nums2 (list[int]): Second list of integers

        Returns:
            list[int]: A list containing [answer1, answer2] where:
                - answer1 is the count of elements in nums1 that exist in nums2
                - answer2 is the count of elements in nums2 that exist in nums1

        Example:
            >>> findIntersectionValues([4,3,2,3,1], [2,2,5,2,3,6])
            [3, 4]  # 3 elements from nums1 exist in nums2, 4 elements from nums2 exist in nums1

        Time complexity: O(n + m) - where n and m are lengths of nums1 and nums2
        Space complexity: O(min(n,m)) - for storing the intersection set

        LeetCode: Beats 96.21% of submissions
        """
        answer1 = 0
        answer2 = 0

        intersec = set(nums1).intersection(set(nums2))

        for num in nums1:
            if num in intersec:
                answer1 += 1

        for num in nums2:
            if num in intersec:
                answer2 += 1

        return [answer1, answer2]
