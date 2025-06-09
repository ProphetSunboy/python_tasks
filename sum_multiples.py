# First solution
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        s = 0

        for num in range(1, n + 1):
            if num % 3 == 0:
                s += num
            elif num % 5 == 0:
                s += num
            elif num % 7 == 0:
                s += num

        return s


# Second solution
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        """Calculates the sum of all integers in range [1, n] that are divisible by 3, 5, or 7.

        Given a positive integer n, returns the sum of all numbers in the range [1, n] inclusive
        that are divisible by 3, 5, or 7.

        Args:
            n (int): The upper bound of the range to check

        Returns:
            int: The sum of all numbers divisible by 3, 5, or 7 in the range

        Example:
            >>> sumOfMultiples(7)
            21  # 3 + 5 + 6 + 7 = 21

        Time complexity: O(n) - where n is the input number
        Space complexity: O(n) - for storing the set of multiples

        LeetCode: Beats 95.10% of submissions
        """
        nums = set()

        nums.update(range(3, n + 1, 3))
        nums.update(range(5, n + 1, 5))
        nums.update(range(7, n + 1, 7))

        return sum(nums)
