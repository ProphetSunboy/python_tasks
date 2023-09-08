class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        """
        Given an integer numRows, return the first numRows of Pascal's triangle.

        :param int numRows: robot movement sequence
        :returns list[list[int]] pt: first numRows of Pascal's triangle

        Time complexity: O(n^2)
        Space complexity: O(n^2)

        LeetCode: Beats 97.61%
        """
        pt = [[1]]

        for i in range(1, numRows):
            currRow = [1]
            currRow.extend([0] * (i - 1))
            currRow.append(1)

            for j in range(1, i):
                currRow[j] = pt[i - 1][j - 1] + pt[i - 1][j]

            pt.append(currRow)

        return pt
