class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        """
        Determine if a given integer n can be represented as the sum of
        distinct powers of three.

        An integer y is a power of three if there exists an integer x such
        that y == 3**x.

        Args:
            n (int): The integer to check.

        Returns:
            bool: True if n can be expressed as the sum of distinct powers of
            three, False otherwise.

        Example:
            Input: n = 12
            Output: True  # 12 = 9 (3**2) + 3 (3**1)

        Time Complexity: O(log n), where n is the given integer.
        Space Complexity: O(1), as only a constant amount of extra space is used.

        LeetCode: Beats 100% of submissions
        """
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3

        return True
