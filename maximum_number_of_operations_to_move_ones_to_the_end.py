class Solution:
    def maxOperations(self, s: str) -> int:
        """
        Calculates the maximum number of operations to move all '1's to the end
        of a given binary string `s` according to the following operation:

        Operation:
            - Choose any index i (where i + 1 < len(s)) such that s[i] == '1' and s[i + 1] == '0'.
            - Move s[i] to the right until it is either at the end of the string or just before another '1'.
              (e.g., for s = "010010" and i = 1, the result is s = "000110")

        The function performs operations greedily and returns the maximum number
        of operations possible.

        Args:
            s (str): Binary string consisting of '0's and '1's.

        Returns:
            int: Maximum number of operations that can be performed.

        Example:
            Input:  s = "1001101"
            Output: 4
            Explanation: After operations, all '1's are moved as far right as possible.

        Time Complexity: O(n), where n is the length of the input string.
        Space Complexity: O(n), used for splitting the string.

        LeetCode: Beats 97.01% of submissions
        """
        ops = 0
        curr_move = 0
        s = s.split("0")

        for i in range(len(s) - 1):
            if s[i] == "":
                continue

            curr_move += len(s[i])
            ops += curr_move

        return ops
