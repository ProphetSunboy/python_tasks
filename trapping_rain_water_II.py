import heapq


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        """
        Calculates the total volume of water that can be trapped after raining on a 2D elevation map.

        Args:
            heightMap (List[List[int]]): An m x n matrix representing the height of each unit cell.

        Returns:
            int: The total volume of trapped water.

        Example:
            >>> trapRainWater([
            ...   [1,4,3,1,3,2],
            ...   [3,2,1,3,2,4],
            ...   [2,3,3,2,3,1]
            ... ])
            4

        Time Complexity: O(m * n * log(m * n)), where m and n are the dimensions of heightMap.
        Space Complexity: O(m * n)
        """
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        min_heap = []

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(min_heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        trapped_water = 0

        while min_heap:
            height, x, y = heapq.heappop(min_heap)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    if heightMap[nx][ny] < height:
                        trapped_water += height - heightMap[nx][ny]
                    heapq.heappush(min_heap, (max(heightMap[nx][ny], height), nx, ny))
                    visited[nx][ny] = True

        return trapped_water
