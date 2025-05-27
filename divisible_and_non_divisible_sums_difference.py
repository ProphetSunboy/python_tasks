class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        """
        Calculate the difference between non-divisible and divisible sums.

        Given positive integers n and m, calculates:
        num1 = sum of numbers from 1 to n that are not divisible by m
        num2 = sum of numbers from 1 to n that are divisible by m
        Returns num1 - num2

        Args:
            n (int): Upper bound of range (inclusive)
            m (int): Divisor to check numbers against

        Returns:
            int: Difference between non-divisible sum and divisible sum

        Time complexity: O(n/m) for the loop iterations
        Space complexity: O(1) as only using constant extra space

        LeetCode: Beats 100% of submissions
        """
        s = n * (n + 1) // 2

        for i in range(m, n + 1, m):
            s -= i * 2

        return s
