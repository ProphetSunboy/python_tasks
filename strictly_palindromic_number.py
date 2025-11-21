class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        """
        Determines if an integer n is strictly palindromic.

        An integer n is strictly palindromic if, for every base b between 2 and
        n - 2 (inclusive), the string representation of n in base b is a
        palindrome (reads the same forward and backward).

        Args:
            n (int): The integer to check for strict palindromicity.

        Returns:
            bool: True if n is strictly palindromic, False otherwise.

        Example:
            Input: n = 9
            Output: False
              # Explanation: 9 is not palindromic in all bases from 3 to 7.

        Time Complexity: O(n^2), since for each base we may use up to O(log n)
        division steps and up to n bases are checked.
        Space Complexity: O(log n), for base conversion at each check.

        LeetCode: Beats 100% of submissions
        """

        def convert_to_base_n(num: int, base: int) -> int:
            res = []

            while num >= base:
                res.append(num % base)
                num //= base

            res.append(num)

            return res[::-1]

        for base in range(2, n - 1):
            curr = convert_to_base_n(n, base)
            if curr != curr[::-1]:
                return False

        return True
