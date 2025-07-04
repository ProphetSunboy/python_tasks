class Solution:
    def largestOddNumber(self, num: str) -> str:
        """Given a string num representing a large integer, return the largest-valued
        odd integer (as a string) that is a non-empty substring of num.
        If no odd integer exists, return an empty string "".

        A substring is a contiguous sequence of characters within a string.

        Args:
            num (str): The string representation of the large integer.

        Returns:
            str: The largest-valued odd integer substring, or "" if none exists.

        Example:
            >>> largestOddNumber("35427")
            '35427'
            >>> largestOddNumber("4206")
            ''

        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 91.05% of submissions
        """
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2:
                return num[: i + 1]
        return ""
