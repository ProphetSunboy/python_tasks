class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        """Finds two positive integers A and B such that:
            - A + B = n
            - Neither A nor B contains the digit '0'

        Args:
            n (int): The target integer to split.

        Returns:
            List[int]: A list [A, B] where both A and B are positive integers without any zero digits.

        Example:
            >>> getNoZeroIntegers(11)
            [2, 9]

        LeetCode: Beats 100% of submissions
        """
        i = 1

        while True:
            if "0" not in str(i) and "0" not in str(n - i):
                break
            i += 1

        return [i, n - i]
