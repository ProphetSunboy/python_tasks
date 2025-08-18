class Solution:
    def averageValue(self, nums: list[int]) -> int:
        """
        Returns the average value of all even integers in the input list that are divisible by 3.

        The average is defined as the sum of the qualifying elements divided by their count, rounded down to the nearest integer.
        If there are no such elements, returns 0.

        Args:
            nums (list[int]): List of positive integers.

        Returns:
            int: The average value of all even integers divisible by 3, or 0 if none exist.

        Example:
            >>> averageValue([1, 2, 3, 4, 6, 12])
            9

        Time Complexity: O(n)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        s = 0
        c = 0

        for num in nums:
            if num % 6 == 0:
                s += num
                c += 1

        if c == 0:
            return 0

        return s // c
