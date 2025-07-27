class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        """Counts the number of hills and valleys in a 0-indexed integer list.

        An index i is part of a hill if its closest non-equal neighbors on both sides are smaller than nums[i].
        An index i is part of a valley if its closest non-equal neighbors on both sides are larger than nums[i].
        Consecutive equal elements are considered part of the same hill or valley.

        An index must have non-equal neighbors on both the left and right to be considered.

        Args:
            nums (list[int]): The input list of integers.

        Returns:
            int: The total number of hills and valleys in nums.

        Example:
            >>> countHillValley([2,4,1,1,6,5])
            3

        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        hill_vall = 0
        prev = nums[0]

        for i in range(1, len(nums) - 1):
            next = nums[i + 1]
            if nums[i] == nums[i - 1]:
                continue
            else:
                j = 2
                while next == nums[i]:
                    if i + j >= len(nums):
                        break
                    next = nums[i + j]
                    j += 1

                if (nums[i] < prev and nums[i] < next) or (
                    nums[i] > prev and nums[i] > next
                ):
                    hill_vall += 1

                prev = nums[i]

        return hill_vall
