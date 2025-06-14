class Solution:
    def countDigits(self, num: int) -> int:
        """Counts the number of digits in a number that divide the number evenly.

        Given a positive integer num, returns how many of its digits are divisors of num.
        A digit d divides num if num % d == 0.

        Args:
            num (int): A positive integer to check

        Returns:
            int: Number of digits in num that divide num evenly

        Examples:
            >>> countDigits(121)
            2  # 1 and 1 divide 121, but 2 does not
            >>> countDigits(1248)
            4  # All digits 1, 2, 4, and 8 divide 1248

        Time complexity: O(n) - where n is number of digits in num
        Space complexity: O(n) - for string conversion and digit list

        LeetCode: Beats 100% of submissions
        """
        digits = map(int, list(str(num)))

        return sum([num % digit == 0 for digit in digits])
