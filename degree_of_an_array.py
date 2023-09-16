class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        """
        Given a non-empty list of non-negative integers nums, find the smallest
        possible length of a (contiguous) subarray, that has the same degree as
        nums.

        The degree of nums is defined as the maximum frequency of any one of its
        elements.

        :param list[int] nums: non-empty list of non-negative integers
        :returns int min_length: smallest possible length of a (contiguous)
        subarray, that has the same degree as nums

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 92.96%
        """
        c = collections.Counter(nums)
        max_freq = 0

        for freq in c.values():
            if freq > max_freq:
                max_freq = freq

        min_length = 10**5
        lengths = {}

        for i, num in enumerate(nums):
            if c[num] == max_freq:
                if lengths.get(num, 0) == 0:
                    lengths[num] = [i, i]
                else:
                    lengths[num] = (lengths[num][0], i)

        for _, length in lengths.items():
            if length[1] - length[0] + 1 < min_length:
                min_length = length[1] - length[0] + 1

        return min_length
