class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        Return an list ans of length nums1.length such that ans[i] is the next
        greater element.

        The next greater element of some element x in an list is the first
        greater element that is to the right of x in the same list.

        You are given two distinct 0-indexed integer lists nums1 and nums2,
        where nums1 is a subset of nums2.

        For each 0 <= i < nums1.length, find the index j such that
        nums1[i] == nums2[j] and determine the next greater element of nums2[j]
        in nums2. If there is no next greater element, then the answer for this
        query is -1.


        :param list[int] nums1: subset of nums2
        :param list[int] nums2: list of distinct integers
        :returns list[int] ans: list of length nums1.length such that ans[i] is
        the next greater element as described above

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 99.34%
        """
        if not nums2:
            return None

        mapping = {}
        result = []
        stack = []
        stack.append(nums2[0])

        for i in range(1, len(nums2)):
            while stack and nums2[i] > stack[-1]:
                mapping[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])

        for element in stack:
            mapping[element] = -1

        for i in range(len(nums1)):
            result.append(mapping[nums1[i]])
        return result
