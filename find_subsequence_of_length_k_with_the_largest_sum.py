class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        """Find a subsequence of length k with the largest sum.

        Given an integer list nums and an integer k, find a subsequence of nums
        of length k that has the largest possible sum. A subsequence is a list
        that can be derived from another list by deleting some or no elements
        without changing the order of the remaining elements.

        Args:
            nums (list[int]): The list of integers to find subsequence from.
            k (int): The length of the desired subsequence.

        Returns:
            list[int]: A subsequence of length k with the largest sum.

        Example:
            >>> maxSubsequence([2, 1, 3, 3], 2)
            [3, 3]
            >>> maxSubsequence([-1, -2, 3, 4], 3)
            [-1, 3, 4]

        LeetCode: Beats 100% of submissions
        """
        sorted_nums = sorted(nums, reverse=True)
        elems_c = Counter(sorted_nums[:k])
        largest_subseq = []

        for num in nums:
            if elems_c.get(num, 0):
                largest_subseq.append(num)
                elems_c[num] -= 1

                if len(largest_subseq) == k:
                    break

        return largest_subseq
