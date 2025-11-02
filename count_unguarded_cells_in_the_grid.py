class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        """
        Calculates the number of unguarded and unoccupied cells in a 0-indexed m x n grid.

        A grid cell may contain either a guard or a wall.
        Guards can see in all four cardinal directions (north, east, south, and west),
        but their vision is blocked by walls or by other guards.
        A cell is considered "guarded" if at least one guard can see it
        (not blocked by a wall or another guard).
        The task is to determine the number of cells that are not occupied by a
        guard or wall, and are not guarded.

        Args:
            m (int): Number of rows in the grid.
            n (int): Number of columns in the grid.
            guards (List[List[int]]): List of [row, col] positions where guards are located.
            walls (List[List[int]]): List of [row, col] positions where walls are located.

        Returns:
            int: The number of cells that are not occupied by guards or walls and that are not guarded.

        Example:
            >>> countUnguarded(
            ...     4, 6,
            ...     guards=[[0,0],[1,1],[2,3]],
            ...     walls=[[0,1],[2,2],[1,4]]
            ... )
            7

        Time Complexity: O(G*(m+n)), where G is the number of guards.
        Space Complexity: O(m*n), due to grid storage.

        LeetCode: Beats 98.47% of submissions
        """
        grid = [[0] * n for _ in range(m)]

        for row, col in walls:
            grid[row][col] = "W"
        for row, col in guards:
            grid[row][col] = "G"

        guarded = 0
        for row, col in guards:
            i = row - 1
            while i >= 0:
                if grid[i][col] == "W" or grid[i][col] == "G":
                    break
                if grid[i][col] == 0:
                    grid[i][col] = 1
                    guarded += 1
                i -= 1

            i = row + 1
            while i < m:
                if grid[i][col] == "W" or grid[i][col] == "G":
                    break
                if grid[i][col] == 0:
                    grid[i][col] = 1
                    guarded += 1
                i += 1

            j = col - 1
            while j >= 0:
                if grid[row][j] == "W" or grid[row][j] == "G":
                    break
                if grid[row][j] == 0:
                    grid[row][j] = 1
                    guarded += 1
                j -= 1

            j = col + 1
            while j < n:
                if grid[row][j] == "W" or grid[row][j] == "G":
                    break
                if grid[row][j] == 0:
                    grid[row][j] = 1
                    guarded += 1
                j += 1

        return (m * n) - guarded - len(guards) - len(walls)
