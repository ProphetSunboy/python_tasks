class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        """
        Given a list nums consisting of positive integers, return the total frequencies of elements in nums that have the maximum frequency.

        The frequency of an element is the number of times it appears in the list.

        Args:
            nums (List[int]): The input list of positive integers.

        Returns:
            int: The sum of the frequencies of all elements that appear the maximum number of times.

        Example:
            >>> maxFrequencyElements([1,2,2,3,1,4])
            4

        Time Complexity: O(N), where N is the length of nums.
        Space Complexity: O(K), where K is the number of unique elements in nums.

        LeetCode: Beats 100% of submissions
        """
        c = Counter(nums)
        max_freq = max(c.values())
        total_freq = 0

        for freq in c.values():
            if freq == max_freq:
                total_freq += freq

        return total_freq
