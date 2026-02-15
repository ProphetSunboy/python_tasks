class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Add two binary strings and return their sum as a binary string.

        Args:
            a (str): First binary string.
            b (str): Second binary string.

        Returns:
            str: The binary sum of a and b.

        Example:
            Input: a = "11", b = "1"
            Output: "100"

        Time Complexity: O(max(len(a), len(b))), since we process each digit of the longer string once.
        Space Complexity: O(max(len(a), len(b))), due to the storage of the sum result.

        LeetCode: Beats 100% of submissions
        """
        return bin(int(a, 2) + int(b, 2))[2:]
