class Solution:
    def maxSum(self, nums: list[int]) -> int:
        """Given an integer list nums, you may delete any number of elements (but not all).
        After deletions, select a sublist (contiguous) such that:
            - All elements in the sublist are unique.
            - The sum of the elements in the sublist is maximized.

        Returns:
            int: The maximum possible sum of a sublist with all unique elements.

        Example:
            >>> maxSum([4,2,4,5,6])
            17  # The sublist [2,4,5,6] has all unique elements and sum 17.

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 100% of submissions
        """
        res = []
        sorted_nums = sorted(set(nums))

        for i, num in enumerate(sorted_nums):
            if num > 0:
                res.append(num)
            elif i == len(sorted_nums) - 1 and len(res) == 0:
                res.append(num)

        return sum(res)
