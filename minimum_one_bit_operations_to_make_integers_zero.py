class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        """
        Given an integer n, transform it into 0 using the minimum number of operations.
        You may perform the following operations any number of times:

        1. Flip the rightmost (0th) bit in the binary representation of n.
        2. Flip the ith bit (i > 0) if and only if the (i-1)th bit is set to 1 and all bits lower than (i-1) are 0.

        This function returns the minimum number of such operations required to turn n into 0.

        Args:
            n (int): The integer to be reduced to 0.

        Returns:
            int: The minimum number of operations required.

        Example:
            Input: n = 3  (binary 11)
            Output: 2
              - Flip the 1st bit: n = 1
              - Flip the 0th bit: n = 0

        Time Complexity: O(log n), where n is the input integer (because the process iterates through bits).
        Space Complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        res = 0
        while n:
            res ^= n
            n >>= 1
        return res
