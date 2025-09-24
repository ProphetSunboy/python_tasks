class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        """
        Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

        If the fractional part is repeating, enclose the repeating part in parentheses.

        If multiple answers are possible, return any of them.

        It is guaranteed that the length of the answer string is less than 10^4 for all the given inputs.

        Args:
            numerator (int): The numerator of the fraction.
            denominator (int): The denominator of the fraction.

        Returns:
            str: The string representation of the fraction. If the fractional part is repeating, the repeating part is enclosed in parentheses.

        Example:
            >>> fractionToDecimal(1, 2)
            '0.5'
            >>> fractionToDecimal(2, 1)
            '2'
            >>> fractionToDecimal(2, 3)
            '0.(6)'
            >>> fractionToDecimal(-50, 8)
            '-6.25'

        Time Complexity: O(n), where n is the length of the fractional part before a repeat occurs (at most denominator different remainders).
        Space Complexity: O(n), for storing seen remainders.

        LeetCode: Beats 100% of submissions
        """
        if numerator % denominator == 0:
            return str(numerator // denominator)

        sign = "-" if (numerator < 0) != (denominator < 0) else ""

        numerator = abs(numerator)
        denominator = abs(denominator)

        result = sign + str(numerator // denominator)
        numerator = numerator % denominator

        if numerator == 0:
            return result

        result += "."

        remainder_map = {}
        fraction_part = ""
        index = 0

        while numerator != 0:
            if numerator in remainder_map:
                start = remainder_map[numerator]
                fraction_part = (
                    fraction_part[:start] + "(" + fraction_part[start:] + ")"
                )
                return result + fraction_part

            remainder_map[numerator] = index

            numerator *= 10
            digit = numerator // denominator
            fraction_part += str(digit)
            numerator = numerator % denominator
            index += 1

        return result + fraction_part
