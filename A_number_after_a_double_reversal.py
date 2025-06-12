# First solution
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        """Checks if a number remains the same after double reversal.

        A double reversal means:
        1. First reverse: Convert number to string, reverse it, and remove leading zeros
        2. Second reverse: Reverse the result of first reversal
        3. Compare if final result equals original number

        Args:
            num (int): The number to check

        Returns:
            bool: True if number remains same after double reversal, False otherwise

        Examples:
            >>> isSameAfterReversals(526)
            True  # 526 -> 625 -> 526
            >>> isSameAfterReversals(1800)
            False  # 1800 -> 81 -> 18

        Time complexity: O(n) - where n is number of digits
        Space complexity: O(n) - for string conversion

        LeetCode: Beats 100% of submissions
        """
        if num == 0:
            return True

        return str(num)[::-1].lstrip("0")[::-1] == str(num)


# Second solution
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num > 0 and num % 10 == 0:
            return False

        return True
