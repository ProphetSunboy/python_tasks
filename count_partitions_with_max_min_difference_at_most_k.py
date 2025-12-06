class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        """
        Given an integer list nums and an integer k, partition nums into one or
        more non-empty contiguous segments such that in each segment, the
        difference between its maximum and minimum elements is at most k.

        Returns the total number of ways to partition nums under this condition.

        The answer should be returned modulo 10**9 + 7.

        Args:
            nums (List[int]): The input list of integers.
            k (int): The maximum allowed difference between the maximum and
            minimum in each segment.

        Returns:
            int: The number of ways to partition nums.

        Example:
            Input: nums = [9,4,1,3,7], k = 4
            Output: 6

        Time Complexity: O(N log N), where N is the number of elements in nums
        (due to balanced tree operations).
        Space Complexity: O(N), for dynamic programming lists.
        """
        n = len(nums)
        mod = 10**9 + 7
        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)
        cnt = SortedList()

        dp[0] = 1
        prefix[0] = 1

        j = 0
        for i in range(n):
            cnt.add(nums[i])

            while j <= i and cnt[-1] - cnt[0] > k:
                cnt.remove(nums[j])
                j += 1
            dp[i + 1] = (prefix[i] - (prefix[j - 1] if j > 0 else 0)) % mod
            prefix[i + 1] = (prefix[i] + dp[i + 1]) % mod

        return dp[n]
