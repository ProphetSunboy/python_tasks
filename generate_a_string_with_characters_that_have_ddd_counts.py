class Solution:
    def generateTheString(self, n: int) -> str:
        """Generates a string of length `n` consisting of lowercase English
        letters such that each character in the string appears an odd number of times.

        If multiple valid strings exist, returns any one of them.

        Args:
            n (int): The length of the string to generate.

        Returns:
            str: A string of length `n` where each character occurs an odd number of times.

        Example:
            >>> generateTheString(4)
            'aaab'  # or any string of length 4 with each character appearing an odd number of times

        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        s = ""

        if n % 2:
            s = "a" * n
        else:
            s = "a" * (n - 1) + "b"

        return s
