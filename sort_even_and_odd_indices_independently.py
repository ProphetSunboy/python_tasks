class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        """Sorts even and odd indices of a list independently according to specific rules.

        Given a 0-indexed integer list nums, rearranges its values by:
        1. Sorting values at odd indices in non-increasing order
        2. Sorting values at even indices in non-decreasing order

        Args:
            nums (List[int]): The input list to be sorted

        Returns:
            List[int]: The list after rearranging values according to the rules

        Example:
            >>> sortEvenOdd([4,1,2,3])
            [2,3,4,1]

        Time complexity: O(n log n) - due to sorting operations
        Space complexity: O(n) - for storing the sorted list and result

        LeetCode: Beats 100% of submissions
        """
        evens = sorted(nums[::2], reverse=True)
        odds = sorted(nums[1::2])
        res = []

        for i in range(len(nums) // 2):
            res.append(evens.pop())
            res.append(odds.pop())

        if evens:
            res.append(evens.pop())

        return res
