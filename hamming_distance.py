class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """
        Given two integers x and y, return the Hamming distance between them.

        The Hamming distance between two integers is the number of positions at
        which the corresponding bits are different.

        :param int x: integer number
        :param int y: integer number
        :returns int hamming_distance: hamming_distance between x and y

        Time complexity: O(1)
        Space complexity: O(1)


        LeetCode: Beats 99.00%
        """
        x_b = bin(x)[2:].zfill(32)
        y_b = bin(y)[2:].zfill(32)

        hamming_distance = 0

        for a, b in zip(x_b, y_b):
            hamming_distance += a != b

        return hamming_distance
