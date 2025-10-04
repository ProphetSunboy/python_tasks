from bisect import bisect_left, insort
from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        """
        Given a 0-indexed list nums of integers, find the minimum possible sum of a mountain triplet.

        A triplet of indices (i, j, k) is a mountain if:
            - i < j < k
            - nums[i] < nums[j] and nums[k] < nums[j]

        Returns the minimum sum of such a triplet. If no such triplet exists, returns -1.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            int: The minimum sum of a mountain triplet, or -1 if none exists.

        Example:
            >>> minimumSum([8,6,1,5,3])
            9

        Time Complexity: O(n log n), where n is the length of nums.
        Space Complexity: O(n)

        LeetCode: Beats 92.43% of submissions
        """
        n = len(nums)
        res = float("inf")

        right_mins = [float("inf")] * n
        sorted_right = []
        for i in range(n - 1, -1, -1):
            right_mins[i] = sorted_right[0] if sorted_right else float("inf")
            if not sorted_right or nums[i] < sorted_right[0]:
                insort(sorted_right, nums[i])

        sorted_left = []
        for j in range(n):
            left_min = float("inf")
            idx = bisect_left(sorted_left, nums[j])
            if idx > 0:
                left_min = sorted_left[0]

            right_min = right_mins[j] if right_mins[j] < nums[j] else float("inf")

            if left_min < nums[j] and right_min < nums[j]:
                res = min(res, left_min + nums[j] + right_min)

            insort(sorted_left, nums[j])

        return res if res != float("inf") else -1
