class Solution:
    def hasTrailingZeros(self, nums: list[int]) -> bool:
        """
        Determines if it is possible to select two or more elements from the input list
        such that the bitwise OR of the selected elements has at least one trailing zero in its binary representation.

        Args:
            nums (List[int]): List of positive integers.

        Returns:
            bool: True if there exists a subset of at least two elements whose bitwise OR has a trailing zero, False otherwise.

        Example:
            >>> hasTrailingZeros([2, 4, 8, 16])
            True
            >>> hasTrailingZeros([1, 3, 5])
            False

        Notes:
            - A trailing zero in binary means the least significant bit is 0.
            - The function checks for any pair or group of numbers whose OR operation results in a number with a trailing zero.

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        seen_trail_zero = False

        for num in nums:
            if bin(num)[-1] == "0":
                if seen_trail_zero:
                    return True
                else:
                    seen_trail_zero = True

        return False
