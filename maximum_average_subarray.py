class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        """
        You are given an integer array nums consisting of n elements, and an
        integer k.

        Find a contiguous subarray whose length is equal to k that has the
        maximum average value and return this value. Any answer with a
        calculation error less than 10-5 will be accepted.

        LeetCode: Beats 97.31%
        """
        max_sum = -(10**5)
        local_sum = sum(nums[:k])

        for i in range(k, len(nums)):
            if local_sum / k > max_sum:
                max_sum = local_sum / k

            local_sum = local_sum - nums[i - k] + nums[i]

        if local_sum / k > max_sum:
            max_sum = local_sum / k

        return max_sum
