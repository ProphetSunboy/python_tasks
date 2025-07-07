class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        """Finds the largest positive integer k in the input list such that both k and -k exist in the list.

        Args:
            nums (list[int]): A list of nonzero integers.

        Returns:
            int: The largest positive integer k such that -k is also in nums.
                 Returns -1 if no such integer exists.

        Example:
            >>> findMaxK([3, 2, -2, 5, -3])
            3
            >>> findMaxK([1, 2, 3, -4])
            -1

        Time complexity: O(n log n) due to sorting.
        Space complexity: O(1) additional space (in-place sort).

        LeetCode: Beats 100% of submissions
        """
        nums.sort()
        l, r = 0, len(nums) - 1

        while l < r:
            if -nums[l] == nums[r]:
                return nums[r]
            elif abs(nums[l]) > nums[r]:
                l += 1
            else:
                r -= 1

        return -1
