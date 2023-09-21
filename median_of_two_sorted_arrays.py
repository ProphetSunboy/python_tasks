class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Given two sorted lists nums1 and nums2 of size m and n respectively,
        return the median of the two sorted lists.

        :param list[int] nums1: sorted list
        :param list[int] nums2: sorted list
        :returns float median: median of nums1 and nums2

        Time complexity: O((n+m)log(n+m))
        Space complexity: O(n+m)

        LeetCode: Beats 93.53%
        """
        nums = nums1 + nums2
        nums.sort()

        if len(nums) % 2:
            return nums[len(nums) // 2]

        return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2
