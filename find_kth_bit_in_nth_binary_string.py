class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        """
        Given two positive integers n and k, the binary string S_n is formed as
        follows:
            S1 = "0"
            Si = Si-1 + "1" + reverse(invert(Si-1)) for i > 1

        Where + denotes concatenation, reverse(x) returns the reversed string x,
        and invert(x) inverts all bits in x (0 becomes 1, and 1 becomes 0).

        For example, the first four strings in the sequence are:
            S1 = "0"
            S2 = "011"
            S3 = "0111001"
            S4 = "011100110110001"

        Return the k-th bit in S_n. It is guaranteed that k is valid for the given n.

        Args:
            n (int): The level of the binary string.
            k (int): The 1-based index of the bit to retrieve.

        Returns:
            str: The k-th bit in S_n ('0' or '1').

        Example:
            Input: n = 3, k = 1
            Output: "0"
            Explanation: S3 is "0111001". The 1st bit is "0".

        Time Complexity: O(log n), since recursion follows the binary structure.
        Space Complexity: O(log n), due to recursion stack.

        LeetCode: Beats 100% of submissions
        """
        if n == 1:
            return "0"

        length = (1 << n) - 1
        mid = (length + 1) // 2

        if k == mid:
            return "1"
        if k < mid:
            return self.findKthBit(n - 1, k)

        c = self.findKthBit(n - 1, length - k + 1)
        return "1" if c == "0" else "0"
