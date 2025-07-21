class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        """Calculates the k-beauty of an integer num.

        The k-beauty of num is defined as the number of substrings of length k (when num is read as a string)
        that are divisors of num. Leading zeros in substrings are allowed. Substrings with value 0 are ignored,
        as 0 is not a divisor of any number.

        Args:
            num (int): The integer to evaluate.
            k (int): The length of substrings to consider.

        Returns:
            int: The k-beauty of num (number of valid substrings).

        Example:
            >>> divisorSubstrings(240, 2)
            2
            # Substrings: "24" and "40"; both are divisors of 240.

        Time complexity: O(n * k), where n is the number of digits in num.
        Space complexity: O(n), for string conversion.

        LeetCode: Beats 100% of submissions
        """
        s_num = str(num)
        k_beauty = 0

        for i in range(len(s_num) - k + 1):
            k_num = int(s_num[i : i + k])

            if k_num == 0:
                continue
            elif num % int(s_num[i : i + k]) == 0:
                k_beauty += 1

        return k_beauty
