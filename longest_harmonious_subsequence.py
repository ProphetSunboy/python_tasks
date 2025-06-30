class Solution:
    def findLHS(self, nums: list[int]) -> int:
        """
        Given an integer list nums, return the length of its longest harmonious
        subsequence among all its possible subsequences.

        We define a harmonious list as an list where the difference between
        its maximum value and its minimum value is exactly 1.

        A subsequence of list is a sequence that can be derived from the list
        by deleting some or no elements without changing the order of the
        remaining elements.

        :param list[int] nums: integer list
        :returns list[list[int]] max_len: len of longest harmonious subsequence

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 98.13%
        """
        c = collections.Counter(nums)
        max_len = 0

        temp = 0
        for num in c:
            if c[num - 1]:
                temp = c[num] + c[num - 1]

                if temp > max_len:
                    max_len = temp

        return max_len


# Second solution
class Solution:
    def findLHS(self, nums: list[int]) -> int:
        """Finds the length of the longest harmonious subsequence.

        A harmonious list is a list where the difference between its maximum
        value and its minimum value is exactly 1. This function finds the
        longest such subsequence in the given `nums` list.

        Args:
            nums (list[int]): The input list of integers.

        Returns:
            int: The length of the longest harmonious subsequence, or 0 if
                 none exists.

        Example:
            >>> findLHS([1,3,2,2,5,2,3,7])
            5
            >>> findLHS([1,2,3,4])
            2
            >>> findLHS([1,1,1,1])
            0

        LeetCode: Beats 99.24% of submissions
        """
        c = Counter(nums)
        longest = 0

        for num, freq in c.items():
            if c.get(num - 1, -(10**4)) + freq > longest:
                longest = c.get(num - 1) + freq

        return longest
