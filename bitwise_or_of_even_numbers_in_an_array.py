class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        """
        Computes the bitwise OR of all even numbers in the input list.

        Given an integer list nums, this method returns the result of
        performing a bitwise OR operation on all even elements of nums.
        If no even numbers are present, returns 0.

        Args:
            nums (List[int]): The list of integers.

        Returns:
            int: The bitwise OR of all even numbers in nums (0 if none).

        Example:
            >>> evenNumberBitwiseORs([3, 1, 4, 2])
            6   # (4 | 2 == 6)
            >>> evenNumberBitwiseORs([1, 3, 5])
            0   # No even numbers present

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        even_or = 0

        for num in nums:
            if num % 2 == 0:
                even_or |= num

        return even_or
