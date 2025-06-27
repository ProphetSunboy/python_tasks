class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        """Given an integer list nums and an integer k, you can repeatedly select any index i and decrement nums[i] by 1.
        Return the minimum number of operations required to make the sum of nums divisible by k.

        Args:
            nums (list[int]): The list of integers to operate on.
            k (int): The divisor.

        Returns:
            int: The minimum number of decrement operations needed.

        Example:
            >>> minOperations([4, 3, 2], 5)
            4

        LeetCode: Beats 100% of submissions
        """
        nums_sum = sum(nums)

        return nums_sum - nums_sum // k * k
