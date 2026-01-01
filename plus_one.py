class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Given a list of integers `digits` representing a non-negative integer
        (with the most significant digit at the head of the list), increment the
        integer by one and return the resulting list of digits.

        The input list does not contain any leading zeros.

        Args:
            digits (List[int]): List of integers between 0 and 9, representing
            the original integer.

        Returns:
            List[int]: List of integers representing the incremented integer.

        Example:
            Input: digits = [1, 2, 3]
            Output: [1, 2, 4]
            # 123 + 1 = 124

            Input: digits = [9, 9, 9]
            Output: [1, 0, 0, 0]
            # 999 + 1 = 1000

        Time Complexity: O(n), where n is the number of digits.
        Space Complexity: O(1), aside from the input and output lists.

        LeetCode: Beats 100% of submissions
        """
        i = len(digits) - 1

        while i >= 0 and digits[i] == 9:
            digits[i] = 0
            i -= 1

        if i == -1:
            digits.insert(0, 1)
        else:
            digits[i] += 1

        return digits
