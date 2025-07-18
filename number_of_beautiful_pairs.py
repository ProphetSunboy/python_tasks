class Solution:
    def countBeautifulPairs(self, nums: list[int]) -> int:
        """Counts the number of beautiful pairs in a 0-indexed integer list `nums`.

        A pair of indices (i, j) with 0 <= i < j < len(nums) is called beautiful if
        the first digit of nums[i] and the last digit of nums[j] are coprime
        (i.e., gcd(first_digit(nums[i]), last_digit(nums[j])) == 1).

        Args:
            nums (list[int]): The input list of integers.

        Returns:
            int: The total number of beautiful pairs in nums.

        Example:
            >>> countBeautifulPairs([2, 5, 1, 4])
            5

        Time complexity: O(n^2) in the naive approach, but this implementation is optimized.
        Space complexity: O(n)

        LeetCode: Beats 99.07% of submissions
        """
        seen = dict()
        pairs = 0

        for num in nums:
            f_digit = int(str(num)[0])
            l_digit = num % 10

            for n, count in seen.items():
                if math.gcd(n, l_digit) == 1:
                    pairs += count

            seen[f_digit] = seen.get(f_digit, 0) + 1

        return pairs


# Another solution
class Solution:
    def digits_are_coprime(self, f_digit: int, l_digit: int) -> bool:
        """Determines if two digits are coprime (i.e., their greatest common divisor is 1).

        Args:
            f_digit (int): The first digit.
            l_digit (int): The second digit.

        Returns:
            bool: True if f_digit and l_digit are coprime, False otherwise.

        This function checks for common divisors between f_digit and l_digit.
        If the only common divisor is 1, they are coprime.
        """
        min_n = min(f_digit, l_digit)
        i = 1
        dividers = 0

        while i <= min_n // 2:
            if f_digit % i == 0 and l_digit % i == 0:
                dividers += 1

            i += 1

        if f_digit % min_n == 0 and l_digit % min_n == 0:
            dividers += 1

        return dividers == 1

    def countBeautifulPairs(self, nums: list[int]) -> int:
        """Counts the number of beautiful pairs in a 0-indexed integer list `nums`.

        A pair of indices (i, j) with 0 <= i < j < len(nums) is called beautiful if
        the first digit of nums[i] and the last digit of nums[j] are coprime
        (i.e., gcd(first_digit(nums[i]), last_digit(nums[j])) == 1).

        Args:
            nums (list[int]): The input list of integers.

        Returns:
            int: The total number of beautiful pairs in nums.

        Example:
            >>> countBeautifulPairs([2, 5, 1, 4])
            5

        # Time complexity: O(n^2), since for each i in 0..n-2, we check all j in i+1..n-1 (nested loop).
        # The coprimes dictionary only helps avoid recomputing coprimality for the same digit pairs,
        # but the number of digit pairs is small (at most 100), so the overall complexity remains O(n^2).
        # Space complexity: O(1), since the coprimes dictionary size is bounded by the number of possible digit pairs (at most 100).
        """
        coprimes = dict()
        pairs = 0

        for i in range(len(nums) - 1):
            f_digit = int(str(nums[i])[0])
            for j in range(i + 1, len(nums)):
                l_digit = nums[j] % 10

                if (f_digit, l_digit) in coprimes:
                    pairs += coprimes[(f_digit, l_digit)]
                else:
                    if self.digits_are_coprime(f_digit, l_digit):
                        pairs += 1
                        coprimes[(f_digit, l_digit)] = 1
                        coprimes[(l_digit, f_digit)] = 1
                    else:
                        coprimes[(f_digit, l_digit)] = 0
                        coprimes[(l_digit, f_digit)] = 0

        return pairs
