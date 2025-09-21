class NeighborSum:
    """
    NeighborSum provides efficient queries for the sum of adjacent or diagonal neighbors
    of a given value in a 2D n x n grid of distinct integers in the range [0, n^2 - 1].

    Methods:
        - __init__(grid: List[List[int]]):
            Initializes the NeighborSum object with the provided grid.

        - adjacentSum(value: int) -> int:
            Returns the sum of elements that are directly adjacent (top, bottom, left, right)
            to the cell containing 'value' in the grid.

        - diagonalSum(value: int) -> int:
            Returns the sum of elements that are diagonally adjacent (top-left, top-right,
            bottom-left, bottom-right) to the cell containing 'value' in the grid.

    Example:
        grid = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]
        ]
        ns = NeighborSum(grid)
        ns.adjacentSum(4)   # Returns 1 + 3 + 5 + 7 = 16
        ns.diagonalSum(4)   # Returns 0 + 2 + 6 + 8 = 16

    Time Complexity:
        - Initialization: O(n^2)
        - Query (adjacentSum/diagonalSum): O(1)

    LeetCode: Beats 95.80% of submissions
    """

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.val_idxs = {
            grid[i][j]: [i, j] for i in range(len(grid)) for j in range(len(grid[0]))
        }

    def adjacentSum(self, value: int) -> int:
        s = 0
        i = self.val_idxs.get(value)[0]
        j = self.val_idxs.get(value)[1]

        if i > 0:
            s += self.grid[i - 1][j]
        if i < len(self.grid) - 1:
            s += self.grid[i + 1][j]
        if j > 0:
            s += self.grid[i][j - 1]
        if j < len(self.grid[0]) - 1:
            s += self.grid[i][j + 1]

        return s

    def diagonalSum(self, value: int) -> int:
        s = 0
        i = self.val_idxs.get(value)[0]
        j = self.val_idxs.get(value)[1]

        if i > 0 and j > 0:
            s += self.grid[i - 1][j - 1]
        if i > 0 and j < len(self.grid[0]) - 1:
            s += self.grid[i - 1][j + 1]
        if i < len(self.grid) - 1 and j > 0:
            s += self.grid[i + 1][j - 1]
        if i < len(self.grid) - 1 and j < len(self.grid[0]) - 1:
            s += self.grid[i + 1][j + 1]

        return s
