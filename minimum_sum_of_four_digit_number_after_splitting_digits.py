class Solution:
    def minimumSum(self, num: int) -> int:
        """Calculates the minimum possible sum of two numbers created by splitting a four-digit number.

        Given a positive integer num with exactly four digits, splits the digits into two new integers
        new1 and new2. All digits must be used, and leading zeros are allowed in both numbers.

        Args:
            num (int): A four-digit positive integer to split

        Returns:
            int: The minimum possible sum of new1 and new2

        Examples:
            >>> minimumSum(2932)
            52  # [23, 29] gives minimum sum
            >>> minimumSum(4009)
            13  # [4, 9] gives minimum sum

        Time complexity: O(n log n) - where n is number of digits (4)
        Space complexity: O(n) - for string conversion and sorting

        LeetCode: Beats 100% of submissions
        """
        l = sorted(list(str(num)))

        return int("".join(l[::2])) + int("".join(l[1::2]))
