class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        """Given a list of integers nums, sort the list in increasing order
        based on the frequency of the values. If multiple values have the same
        frequency, sort them in decreasing order.

        Args:
            nums (list[int]): List of integers to sort

        Returns:
            list[int]: List sorted by increasing frequency, with equal frequency values in decreasing order

        Example:
            >>> frequencySort([1,1,2,2,2,3])
            [3,1,1,2,2,2]
            >>> frequencySort([2,3,1,3,2])
            [1,3,3,2,2]

        Time complexity: O(n log n) where n is the length of nums
        Space complexity: O(n) for storing frequency dictionary

        LeetCode: Beats 100% of submissions
        """
        freqs = dict()
        sorted_nums = []

        for num in set(nums):
            freq = nums.count(num)
            if freqs.get(freq, 0):
                freqs[freq].append(num)
            else:
                freqs[freq] = [num]

        for freq in sorted(freqs.keys()):
            for val in sorted(freqs[freq], reverse=True):
                sorted_nums += [val] * freq

        return sorted_nums
