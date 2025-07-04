class Solution:
    def findGCD(self, nums: list[int]) -> int:
        """Given an integer list nums, return the greatest common divisor (GCD) of the smallest and largest numbers in nums.

        The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

        Args:
            nums (list[int]): The list of integers.

        Returns:
            int: The GCD of the smallest and largest numbers in nums.

        Example:
            >>> findGCD([2, 5, 6, 9, 10])
            2
            >>> findGCD([7, 5, 6, 8, 3])
            1

        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        min_n = min(nums)
        max_n = max(nums)

        i = min_n
        while i > 1:
            if min_n % i == 0 and max_n % i == 0:
                break
            i -= 1

        return i
