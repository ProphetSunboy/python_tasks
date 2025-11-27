class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        """
        Given a list of integers nums and an integer k, returns the maximum sum
        of a sublist of nums such that the size of the sublist is divisible by k.

        Args:
            nums (List[int]): The list of integers.
            k (int): The divisor for the sublist length.

        Returns:
            int: The maximum sum of a sublist with length divisible by k.

        Example:
            Input: nums = [2, 1, 3, -2, 4], k = 3
            Output: 6
            Explanation: The sublist [2, 1, 3] has length 3 (divisible by 3) and sum 6.

        Time Complexity: O(N), where N is the length of nums.
        Space Complexity: O(k)
        """
        n = len(nums)
        prefixSum = 0
        maxSum = -sys.maxsize
        kSum = [sys.maxsize // 2] * k
        kSum[k - 1] = 0
        for i in range(n):
            prefixSum += nums[i]
            maxSum = max(maxSum, prefixSum - kSum[i % k])
            kSum[i % k] = min(kSum[i % k], prefixSum)
        return maxSum
