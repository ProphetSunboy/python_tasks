class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        """
        Simulates walking in a clockwise spiral on a rows x cols grid, starting
        from (rStart, cStart) and initially facing east.
        The walk continues even when temporarily moving outside the grid
        boundaries, and terminates after visiting every valid cell.

        Args:
            rows (int): Number of rows in the grid.
            cols (int): Number of columns in the grid.
            rStart (int): Starting row index.
            cStart (int): Starting column index.

        Returns:
            List[List[int]]: List of [row, column] positions visited in the
            order of the spiral traversal.

        Example:
            Input: rows = 1, cols = 4, rStart = 0, cStart = 0
            Output: [[0,0],[0,1],[0,2],[0,3]]

        Time Complexity: O(rows * cols)
        Space Complexity: O(rows * cols)
        """
        coordinates = [[rStart, cStart]]

        i, j = rStart, cStart

        curr_step = 1

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0

        while len(coordinates) < rows * cols:
            for _ in range(curr_step):
                i += directions[dir_idx][0]
                j += directions[dir_idx][1]

                if 0 <= i < rows and 0 <= j < cols:
                    coordinates.append([i, j])

            dir_idx = (dir_idx + 1) % 4

            if dir_idx == 0 or dir_idx == 2:
                curr_step += 1

        return coordinates
