class Solution:
    def isBalanced(self, num: str) -> bool:
        """Determines if a string of digits is balanced.

        A string is considered balanced if the sum of the digits at even indices
        is equal to the sum of the digits at odd indices.

        Args:
            num (str): The input string consisting only of digits.

        Returns:
            bool: True if the string is balanced, False otherwise.

        Example:
            >>> isBalanced("1232")
            True
            >>> isBalanced("1230")
            False

        LeetCode: Beats 100% of submissions
        """
        even_sum = 0
        odd_sum = 0

        for i, num in enumerate(num):
            if i % 2:
                odd_sum += int(num)
            else:
                even_sum += int(num)

        return even_sum == odd_sum
