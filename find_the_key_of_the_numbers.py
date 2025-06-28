class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        """Generate a four-digit key from three positive integers.

        The key is constructed by taking the minimum digit at each position (1-4)
        from the three numbers after padding with leading zeros to four digits.

        Args:
            num1 (int): First positive integer.
            num2 (int): Second positive integer.
            num3 (int): Third positive integer.

        Returns:
            int: The generated four-digit key without leading zeros.

        Example:
            >>> generateKey(123, 456, 789)
            123
            >>> generateKey(1, 2, 3)
            1

        LeetCode: Beats 100% of submissions
        """
        str_num1 = str(num1).rjust(4, "0")
        str_num2 = str(num2).rjust(4, "0")
        str_num3 = str(num3).rjust(4, "0")

        key = ""

        for i in range(4):
            key += min(str_num1[i], str_num2[i], str_num3[i])

        return int(key)
