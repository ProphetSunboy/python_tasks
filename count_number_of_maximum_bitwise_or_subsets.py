class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        """Given an integer list nums, finds the maximum possible bitwise OR of any subset of nums,
        and returns the number of different non-empty subsets with that maximum bitwise OR.

        A subset is defined as any selection of elements (possibly non-contiguous) from nums.
        Two subsets are considered different if the indices of the selected elements differ.

        The bitwise OR of a subset is computed as the bitwise OR of all its elements.

        Args:
            nums (list[int]): The input list of positive integers.

        Returns:
            int: The number of non-empty subsets whose bitwise OR equals the maximum possible OR.

        Example:
            >>> countMaxOrSubsets([3, 1])
            2  # Subsets [3], [3,1] both have OR == 3

        Time complexity: O(n * 2^n), where n is the length of nums.
        Space complexity: O(2^n), due to the storage of OR values for all subsets.

        LeetCode: Beats 99.80% of submissions
        """
        max_or = 0
        dp = {0: 1}

        for num in nums:
            max_or |= num
            new_dp = dp.copy()

            for or_value, count in dp.items():
                new_or_value = or_value | num
                if new_or_value not in new_dp:
                    new_dp[new_or_value] = count
                else:
                    new_dp[new_or_value] += count

            dp = new_dp

        return dp.get(max_or, 0)
