class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        """
        Given two integers n and start, computes the bitwise XOR of a list nums
        where nums[i] = start + 2 * i for 0 <= i < n.

        Args:
            n (int): The length of the list.
            start (int): The starting integer for the sequence.

        Returns:
            int: The result of XOR-ing all elements in the constructed list.

        Example:
            >>> xorOperation(5, 0)
            8
            >>> xorOperation(4, 3)
            8

        Time Complexity: O(n), where n is the length of the list.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        xor = 0

        for i in range(n):
            xor ^= start + 2 * i

        return xor
