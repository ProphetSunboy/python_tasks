class Solution:
    def isPossibleToSplit(self, nums: list[int]) -> bool:
        """Determines if it is possible to split the given integer list nums (of even length)
        into two parts nums1 and nums2 such that:
            - len(nums1) == len(nums2) == len(nums) // 2
            - nums1 contains only distinct elements
            - nums2 contains only distinct elements

        Args:
            nums (list[int]): The input integer list of even length.

        Returns:
            bool: True if such a split is possible, False otherwise.

        Example:
            >>> isPossibleToSplit([1,2,3,4])
            True
            >>> isPossibleToSplit([1,1,1,2])
            False

        Time complexity: O(n), where n is the length of nums.
        Space complexity: O(n)

        LeetCode: Beats 100% of submissions
        """
        c = Counter(nums)

        for freq in c.values():
            if freq > 2:
                return False

        return True
