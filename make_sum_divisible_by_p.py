class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        """
        Given a list of positive integers nums and an integer p, this function finds
        the length of the smallest (non-whole) sublist you can remove so that the sum
        of the remaining elements is divisible by p. If it is not possible, returns -1.

        Args:
            nums (List[int]): The input list of positive integers.
            p (int): The modulus to check divisibility against.

        Returns:
            int: The minimum length of sublist to remove, or -1 if not possible.

        Example:
            Input: nums = [3, 1, 4, 2], p = 6
            Output: 1
            Explanation: Remove [4] to get sum 6, which is divisible by 6.

        Time Complexity: O(n)
        Space Complexity: O(n)

        LeetCode: Beats 94.75% of submissions
        """
        total_sum = sum(nums)
        target = total_sum % p

        if target == 0:
            return 0

        prefix = 0
        min_len = len(nums) + 1

        remainder_map = {0: -1}

        for i, num in enumerate(nums):
            prefix += num
            remainder = prefix % p

            complement = (remainder - target) % p

            if complement in remainder_map:
                min_len = min(min_len, i - remainder_map[complement])

            remainder_map[remainder] = i

        return min_len if min_len < len(nums) else -1
