import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        Given an n x n integer matrix grid where grid[i][j] represents the elevation at point (i, j):

        - It starts raining, and water level rises over time. At time t, the water
        level is t, so any cell with elevation <= t is submerged or reachable.
        - You can swim from one cell to a 4-directionally adjacent cell if both cells have elevation <= t at the current time.
        - You must stay within the grid boundaries.

        The task is to return the minimum time t required to reach the bottom-right cell (n-1, n-1) from the top-left cell (0, 0).

        Args:
            grid (List[List[int]]): 2D list representing the elevation map.

        Returns:
            int: The minimum time required to reach the bottom-right cell.

        Example:
            >>> swimInWater([[0,2],[1,3]])
            3

        Time Complexity: O(n^2 * log n), where n is the grid size.
        Space Complexity: O(n^2)

        LeetCode: Beats 99.09% of submissions
        """
        n = len(grid)

        min_heap = [(grid[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        result = 0

        while min_heap:
            height, x, y = heapq.heappop(min_heap)

            result = max(result, height)

            if x == n - 1 and y == n - 1:
                return result

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    heapq.heappush(min_heap, (grid[nx][ny], nx, ny))

        return -1
