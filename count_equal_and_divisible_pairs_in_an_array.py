class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        """Counts the number of pairs (i, j) in the list such that:
            - 0 <= i < j < n
            - nums[i] == nums[j]
            - (i * j) is divisible by k

        Args:
            nums (list[int]): The input list of integers.
            k (int): The divisor for the product of indices.

        Returns:
            int: The number of valid pairs satisfying the above conditions.

        Example:
            >>> countPairs([3,1,2,2,2,1,3], 2)
            4

        Time complexity: O(N^2) in the worst case, where N is the length of nums.
        Space complexity: O(N), for storing indices of seen numbers.

        LeetCode: Beats 100% of submissions
        """
        pairs = 0
        seen = dict()

        for i, num in enumerate(nums):
            for idx in seen.get(num, []):
                if (i * idx) % k == 0:
                    pairs += 1

            seen[num] = seen.get(num, []) + [i]

        return pairs
