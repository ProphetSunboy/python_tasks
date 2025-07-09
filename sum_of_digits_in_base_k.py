class Solution:
    def sumBase(self, n: int, k: int) -> int:
        """Returns the sum of the digits of integer n after converting it from base 10 to base k.

        Each digit in the base k representation is treated as a base 10 number, and their sum is returned.

        Args:
            n (int): The integer in base 10 to be converted.
            k (int): The base to convert n into (k >= 2).

        Returns:
            int: The sum of the digits of n in base k, as a base 10 integer.

        Example:
            >>> sumBase(34, 6)
            9
            # 34 in base 6 is 54, and 5 + 4 = 9

        Time complexity: O(log_k(n)), where n is the input number and k is the base.
        Space complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        base_k_sum = 0

        while n >= k:
            base_k_sum += n % k
            n //= k

        base_k_sum += n

        return base_k_sum
