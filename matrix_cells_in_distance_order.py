class Solution:
    def allCellsDistOrder(
        self, rows: int, cols: int, rCenter: int, cCenter: int
    ) -> list[list[int]]:
        """
        You are given four integers row, cols, rCenter, and cCenter. There is a
        rows x cols matrix and you are on the cell with the coordinates
        (rCenter, cCenter).

        Return the coordinates of all cells in the matrix, sorted by their
        distance from (rCenter, cCenter) from the smallest distance to the
        largest distance. You may return the answer in any order that satisfies
        this condition.

        The distance between two cells (r1, c1) and (r2, c2) is
        |r1 - r2| + |c1 - c2|.

        :param int rows: number of rows in matrix
        :param int cols: number of columns in matrix
        :param int rCenter: row coordinate in matrix
        :param int cCenter: column coordinate in matrix
        :returns list[list[int]] ans: coordinates of all cells in the matrix,
        sorted by their distance from (rCenter, cCenter)

        Time complexity: O(n^2)
        Space complexity: O(n^2)

        LeetCode: Beats 91.60%
        """
        dist = set()

        for i in range(rows):
            for j in range(cols):
                dist.add((i, j, abs(i - rCenter) + abs(j - cCenter)))

        return [[i, j] for i, j, _ in sorted(dist, key=lambda item: item[2])]
