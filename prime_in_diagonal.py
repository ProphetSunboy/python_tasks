class Solution:
    def is_prime(self, num: int) -> bool:
        """Given num, return True if it's prime number, False otherwise."""
        i = 3
        if (num % 2 == 0 and num != 2) or num < 2:
            return False
        for _ in range(int(num ** 0.5) + 1):
            if (num / i) % 1 == 0:
                return False
            i += 1
        return True

    def diagonalPrime(self, nums: List[List[int]]) -> int:
        """
        Given a 0-indexed two-dimensional integer array nums.

        Return the largest prime number that lies on at least one of the
        diagonals of nums. In case, no prime is present on any of the
        diagonals, return 0.
        {Beats 99.23%}
        """
        diagonal_vals = []
        for i in range(len(nums)):
            diagonal_vals.append(nums[i][i])
            diagonal_vals.append(nums[i][len(nums)-i-1])

        for num in sorted(diagonal_vals, reverse=True):
            if self.is_prime(num):
                return num
        return 0