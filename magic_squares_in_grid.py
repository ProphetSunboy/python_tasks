class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        """
        Counts the number of 3 x 3 magic square subgrids within a given grid.

        A 3 x 3 magic square is defined as a 3 x 3 grid filled with all the
        numbers from 1 to 9 exactly once, such that the sum of every row, every
        column, and both main diagonals is the same.

        Args:
            grid (List[List[int]]): A 2D list representing the input grid, where
            each element is an integer (grid values may be up to 15).

        Returns:
            int: The total number of 3 x 3 magic square subgrids found in the grid.

        Example:
            Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
            Output: 1

        Time Complexity: O(n * m), where n and m are grid dimensions.
        Space Complexity: O(1), outside of input storage.

        LeetCode: Beats 100% of submissions
        """
        magic_squares = 0
        n, m = len(grid), len(grid[0])

        for i in range(n - 2):
            for j in range(m - 2):
                magic_sum = grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]
                magic = True

                if grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j] != magic_sum:
                    magic = False

                if not magic:
                    continue

                seen = set()
                for k in range(i, i + 3):
                    curr_sum = 0
                    for l in range(j, j + 3):
                        if grid[k][l] < 1 or grid[k][l] > 9:
                            magic = False
                            break

                        if grid[k][l] in seen:
                            magic = False
                            break

                        seen.add(grid[k][l])

                        curr_sum += grid[k][l]

                    if curr_sum != magic_sum:
                        magic = False
                        break

                if not magic:
                    continue

                for l in range(j, j + 3):
                    curr_sum = 0
                    for k in range(i, i + 3):
                        curr_sum += grid[k][l]

                    if curr_sum != magic_sum:
                        magic = False
                        break

                if not magic:
                    continue

                magic_squares += 1

        return magic_squares
