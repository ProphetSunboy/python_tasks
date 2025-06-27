class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        """Given a list of integers nums containing numbers from 0 to n - 1, where each number should appear exactly once,
        but two numbers appear twice (i.e., two numbers are duplicated), find and return the two duplicated numbers.

        Args:
            nums (list[int]): The list of integers with two numbers duplicated.

        Returns:
            list[int]: A list containing the two duplicated numbers (order does not matter).

        Example:
            >>> getSneakyNumbers([0, 1, 2, 3, 2, 4, 5, 1])
            [2, 1]

        LeetCode: Beats 100% of submissions
        """
        c = Counter(nums)
        extra_nums = []

        for num, freq in c.items():
            if freq == 2:
                extra_nums.append(num)

        return extra_nums
