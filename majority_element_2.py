class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        """
        Given an integer array of size n, find all elements that appear more
        than n/3 times.

        :param list[int] nums: list of integers
        :returns list[int] majority: elements that appear more than n/3 times

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 97.24%
        """
        majority = []
        freqs = {}

        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1

        for num, freq in freqs.items():
            if freq > len(nums) // 3:
                majority.append(num)

        return majority
