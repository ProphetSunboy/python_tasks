class Solution:
    def get_digit_sum(self, num: int) -> int:
        """Calculate the sum of all digits in a given integer.

        Args:
            num (int): The integer whose digits need to be summed.

        Returns:
            int: The sum of all digits in the input integer.

        Example:
            >>> get_digit_sum(123)
            6
            >>> get_digit_sum(456)
            15
            >>> get_digit_sum(999)
            27

        Time complexity: O(log(num)) where num is the input integer
        Space complexity: O(1) as we only use a constant amount of extra space
        """
        digit_sum = 0

        while num > 0:
            digit_sum += num % 10
            num //= 10

        return digit_sum

    def getLucky(self, s: str, k: int) -> int:
        """Given a string s consisting of lowercase English letters and an integer k,
        convert the string into an integer by replacing each letter with its position
        in the alphabet, then transform it by summing its digits k times.

        Args:
            s (str): A string of lowercase English letters.
            k (int): The number of times to transform the integer by summing its digits.

        Returns:
            int: The resulting integer after performing the conversion and k transformations.

        Example:
            >>> getLucky("zbax", 2)
            8
            >>> getLucky("leetcode", 2)
            6
            >>> getLucky("iiii", 1)
            36

        Time complexity: O(n + k * log(num)) where n is string length and num is the converted integer
        Space complexity: O(log(num)) for storing the converted integer as string

        LeetCode: Beats 100% of submissions
        """
        num = ""

        for ch in s:
            num += str(ord(ch) - 96)

        num = int(num)

        while k > 0:
            num = self.get_digit_sum(num)
            k -= 1

        return num
