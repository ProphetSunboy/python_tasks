class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        """
        Removes exactly one occurrence of the specified digit from the given number
        string to maximize the resulting value.

        Args:
            number (str): The string representation of a positive integer.
            digit (str): The digit character to remove (guaranteed to appear at least once in number).

        Returns:
            str: The resulting string after removing one occurrence of digit to maximize the decimal value.

        Example:
            >>> removeDigit("1231", "1")
            '231'
            >>> removeDigit("551", "5")
            '51'

        Time Complexity: O(n), where n is the length of number.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        c = number.count(digit)

        for i in range(len(number)):
            if number[i] == digit:
                if c == 1 or number[i] < number[i + 1]:
                    return number[:i] + number[i + 1 :]
                else:
                    c -= 1
