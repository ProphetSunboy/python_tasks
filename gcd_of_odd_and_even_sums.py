class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        """
        Given an integer n, compute the GCD (greatest common divisor) of:
            - sumOdd: the sum of the first n odd numbers
            - sumEven: the sum of the first n even numbers

        The first n odd numbers are: 1, 3, 5, ..., (2n-1)
        The first n even numbers are: 2, 4, 6, ..., (2n)

        sumOdd = n^2
        sumEven = n * (n + 1)

        Args:
            n (int): The number of terms to consider for both odd and even sums.

        Returns:
            int: The GCD of sumOdd and sumEven.

        Example:
            >>> gcdOfOddEvenSums(4)
            4

        Time Complexity: O(log n), due to the use of the Euclidean algorithm for GCD.
        Space Complexity: O(1), as only a constant amount of extra space is used.

        LeetCode: Beats 100% of submissions
        """
        sum_odd = n**2
        sum_even = n * (n + 1)

        return math.gcd(sum_odd, sum_even)
