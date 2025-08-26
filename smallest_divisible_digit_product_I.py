class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        """
        Given two integers n and t, returns the smallest integer x such that:
            - x >= n
            - The product of the digits of x is divisible by t.

        Args:
            n (int): The lower bound integer.
            t (int): The divisor for the product of digits.

        Returns:
            int: The smallest integer >= n whose digits' product is divisible by t.

        Example:
            >>> smallestNumber(12, 6)
            16
            >>> smallestNumber(14, 2)
            14

        Time Complexity: O(k * d), where k is the number of candidates checked and d is the number of digits in each candidate.
        Space Complexity: O(d), for digit extraction.

        LeetCode: Beats 100% of submissions
        """
        curr = n

        while True:
            if math.prod(map(int, str(curr))) % t == 0:
                return curr

            curr += 1
