class Solution:
    def digitCount(self, num: str) -> bool:
        """
        Checks if the given string num is a 'self-describing' number.

        A self-describing number is defined as a string where, for every index i (0 <= i < n),
        the digit i appears exactly num[i] times in num.

        Args:
            num (str): A string of digits.

        Returns:
            bool: True if num is self-describing, False otherwise.

        Example:
            >>> digitCount("1210")
            True
            >>> digitCount("030")
            False

        Time Complexity: O(n), where n is the length of num.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        c = Counter(num)

        for i, n in enumerate(num):
            if c[str(i)] != int(n):
                return False

        return True
