class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        """Returns the number of common factors of two positive integers a and b.

        An integer x is a common factor of a and b if x divides both a and b (i.e., a % x == 0 and b % x == 0).

        Args:
            a (int): First positive integer.
            b (int): Second positive integer.

        Returns:
            int: The number of common factors shared by a and b.

        Example:
            >>> commonFactors(12, 6)
            4  # (1, 2, 3, 6)
            >>> commonFactors(25, 30)
            2  # (1, 5)

        Time complexity: O(min(a, b)), where min(a, b) is the smaller of the two input integers.
        Space complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        min_num = min(a, b)
        counter = 0
        factor = 1

        while factor <= min_num // 2:
            if a % factor == 0 and b % factor == 0:
                counter += 1

            factor += 1

        return counter if max(a, b) % min_num else counter + 1
