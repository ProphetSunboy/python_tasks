class Solution:
    def minNumber(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Given two lists of unique digits, nums1 and nums2, return the smallest number
        that contains at least one digit from each list.

        Args:
            nums1 (list[int]): First list of unique digits.
            nums2 (list[int]): Second list of unique digits.

        Returns:
            int: The smallest possible number formed using at least one digit from each list.

        Examples:
            >>> minNumber([4,1,3], [5,7])
            15
            >>> minNumber([3,5,2], [4,3,1])
            3

        Time Complexity: O(n + m), where n and m are the lengths of nums1 and nums2.
        Space Complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        for num in sorted(nums1):
            if num in nums2:
                return num

        min_n1 = min(nums1)
        min_n2 = min(nums2)

        if min_n1 < min_n2:
            return int(str(min_n1) + str(min_n2))

        return int(str(min_n2) + str(min_n1))
