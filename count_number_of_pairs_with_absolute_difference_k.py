class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        """Counts the number of pairs (i, j) in the list such that:
            - 0 <= i < j < n
            - |nums[i] - nums[j]| == k

        Args:
            nums (list[int]): The input list of integers.
            k (int): The absolute difference to check for.

        Returns:
            int: The number of valid pairs with absolute difference k.

        Example:
            >>> countKDifference([1,2,2,1], 1)
            4

        Time complexity: O(N), where N is the length of nums.
        Space complexity: O(N), for storing counts of seen numbers.

        LeetCode: Beats 100% of submissions
        """
        pairs = 0
        seen = dict()

        for num in nums:
            pairs += seen.get(num - k, 0) + seen.get(k + num, 0)
            seen[num] = seen.get(num, 0) + 1

        return pairs
