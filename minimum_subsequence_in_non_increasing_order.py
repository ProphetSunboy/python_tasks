class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        """Find a minimum subsequence with sum greater than remaining elements.

        Given a list nums, find a subsequence whose sum is strictly greater than
        the sum of the non-included elements. If multiple solutions exist, return
        the one with minimum size. If still multiple solutions exist, return the
        one with maximum total sum. The result is guaranteed to be unique and
        should be returned in non-increasing order.

        A subsequence is obtained by erasing some (possibly zero) elements from
        the list without changing the order of remaining elements.

        Args:
            nums (list[int]): The list of integers to find subsequence from.

        Returns:
            list[int]: A subsequence with sum greater than remaining elements,
                      sorted in non-increasing order.

        Example:
            >>> minSubsequence([4, 3, 10, 9, 8])
            [10, 9]
            >>> minSubsequence([6])
            [6]

        LeetCode: Beats 100% of submissions
        """
        sorted_nums = sorted(nums, reverse=True)
        total_s = sum(nums)
        curr_s = 0
        res = []
        i = 0

        while curr_s <= total_s:
            curr_s += sorted_nums[i]
            total_s -= sorted_nums[i]
            res.append(sorted_nums[i])
            i += 1

        return res
