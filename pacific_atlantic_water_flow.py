class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Given an m x n matrix heights representing the height above sea level at
        each cell (r, c) of an island, return a list of grid coordinates where water
        can flow to both the Pacific and Atlantic oceans.

        The Pacific Ocean touches the island's left and top edges, and the
        Atlantic Ocean touches the island's right and bottom edges.
        Water can flow from a cell to another cell if the next cell's height is
        less than or equal to the current cell's height, and the two cells are
        adjacent (north, south, east, or west).

        Args:
            heights (List[List[int]]): 2D matrix of integers representing cell heights.

        Returns:
            List[List[int]]: List of [row, col] coordinates where water can flow to both oceans.

        Example:
            >>> heights = [
            ...   [1,2,2,3,5],
            ...   [3,2,3,4,4],
            ...   [2,4,5,3,1],
            ...   [6,7,1,4,5],
            ...   [5,1,1,2,4]
            ... ]
            >>> pacificAtlantic(heights)
            [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]

        Time Complexity: O(m * n), where m and n are the dimensions of heights.
        Space Complexity: O(m * n)

        LeetCode: Beats 98.20% of submissions
        """
        if not heights:
            return []

        m, n = len(heights), len(heights[0])

        pacific_reach = [[False] * n for _ in range(m)]
        atlantic_reach = [[False] * n for _ in range(m)]

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c, ocean_reach, prev_height):
            if (
                r < 0
                or r >= m
                or c < 0
                or c >= n
                or ocean_reach[r][c]
                or heights[r][c] < prev_height
            ):
                return
            ocean_reach[r][c] = True
            for dr, dc in directions:
                dfs(r + dr, c + dc, ocean_reach, heights[r][c])

        for i in range(m):
            dfs(i, 0, pacific_reach, heights[i][0])
            dfs(i, n - 1, atlantic_reach, heights[i][n - 1])

        for j in range(n):
            dfs(0, j, pacific_reach, heights[0][j])
            dfs(m - 1, j, atlantic_reach, heights[m - 1][j])

        result = []
        for i in range(m):
            for j in range(n):
                if pacific_reach[i][j] and atlantic_reach[i][j]:
                    result.append([i, j])

        return result
