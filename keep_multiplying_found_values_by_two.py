# First solution
class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        """Given a list of integers `nums` and an integer `original`, repeatedly double `original` as long as it is found in `nums`.
        Return the final value of `original` after this process.

        Args:
            nums (list[int]): The list of integers to search within.
            original (int): The starting integer to search for and double.

        Returns:
            int: The resulting value of `original` after all possible doublings.

        Example:
            >>> findFinalValue([5,3,6,1,12], 3)
            24

        Time complexity: O(n + k), where n is the length of nums and k is the number of doublings.
        Space complexity: O(n)

        LeetCode: Beats 100% of submissions
        """
        nums_d = {num: 1 for num in nums}

        while nums_d.get(original, 0):
            original *= 2

        return original


# Second solution
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        """
        LeetCode: Beats 100% of submissions
        """
        nums_set = set(nums)

        while original in nums_set:
            original *= 2

        return original
