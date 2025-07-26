class Solution:
    def isFascinating(self, n: int) -> bool:
        """Determines if a 3-digit integer n is a fascinating number.

        A number n is called fascinating if, after concatenating n, 2*n, and 3*n (in that order),
        the resulting 9-digit number contains all digits from 1 to 9 exactly once (no zeros).

        Args:
            n (int): A 3-digit integer.

        Returns:
            bool: True if n is fascinating, False otherwise.

        Example:
            >>> isFascinating(192)
            True  # 192 + 384 + 576 = '192384576', which contains all digits 1-9 exactly once.

        Time complexity: O(1)
        Space complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        num = str(n) + str(n * 2) + str(n * 3)

        return "".join(sorted(num)) == "123456789"
