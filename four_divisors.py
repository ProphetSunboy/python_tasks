class Solution:
    def sumFourDivisors(self, nums):
        """
        Return the sum of all numbers in the input list that have exactly four
        divisors.

        Args:
            nums (List[int]): List of positive integers.

        Returns:
            int: Sum of all numbers in nums that have exactly four divisors,
                 where for each such number, the sum of its four divisors is added.

        Example:
            Input:
                nums = [21, 4, 7]
            Output:
                32
            Explanation:
                21 has four divisors: 1, 3, 7, 21 (sum = 32)
                4 has three divisors: 1, 2, 4
                7 has two divisors: 1, 7

        Time Complexity: O(m * sqrt(n)), where m = len(nums) and n is the
        largest number in nums.
        Space Complexity: O(1), excluding input and output.
        """

        def is_prime(x):
            if x < 2:
                return False
            i = 2
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 1
            return True

        total = 0

        for n in nums:
            p = round(n ** (1 / 3))
            if p**3 == n and is_prime(p):
                total += 1 + p + p * p + n
                continue

            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    j = n // i
                    if i != j and is_prime(i) and is_prime(j):
                        total += 1 + i + j + n
                    break

        return total
