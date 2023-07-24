from math import factorail as fact
from math import prod


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        """
        Given an integer rowIndex, return the rowIndexth (0-indexed) row of the
        Pascal's triangle.

        LeetCode: Beats 98.96%
        """
        if rowIndex == 0:
            return [1]

        bin_coeffs = [0] * (rowIndex + 1)

        for i in range(rowIndex // 2 + 1):
            bin_coeffs[i] = prod(range(max(i, rowIndex - i) + 1, rowIndex + 1)) // fact(
                min(i, rowIndex - i)
            )

        if len(bin_coeffs) % 2:
            bin_coeffs[i + 1 :] = bin_coeffs[:i][::-1]
        else:
            bin_coeffs[i + 1 :] = bin_coeffs[: i + 1][::-1]

        return bin_coeffs
