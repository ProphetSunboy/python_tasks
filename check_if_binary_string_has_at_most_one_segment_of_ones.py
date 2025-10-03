class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        """
        Determines if a binary string contains at most one contiguous segment of ones.

        Args:
            s (str): A binary string without leading zeros.

        Returns:
            bool: True if there is at most one contiguous segment of ones, False otherwise.

        Example:
            >>> checkOnesSegment("110")
            True
            >>> checkOnesSegment("1001")
            False

        Time Complexity: O(n), where n is the length of the string.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        ones = False

        for i, n in enumerate(s):
            if n == "1":
                if not ones:
                    ones = True
                elif s[i - 1] == "1":
                    continue
                else:
                    return False

        return True
