class Solution:
    def nearestmin_validPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        """
        Finds the index of the nearest valid point that shares the same x or y coordinate.

        A point is considered valid if it shares either the same x-coordinate or the same y-coordinate
        as the given location (x, y). Among all valid points, the function returns the index of the one
        with the smallest Manhattan distance to (x, y). If there are multiple such points, the one with
        the smallest index is returned. If no valid point exists, returns -1.

        The Manhattan distance between (x1, y1) and (x2, y2) is defined as abs(x1 - x2) + abs(y1 - y2).

        Args:
            x (int): The x-coordinate of the current location.
            y (int): The y-coordinate of the current location.
            points (List[List[int]]): List of points, where each point is [ai, bi].

        Returns:
            int: The index of the nearest valid point, or -1 if none exists.

        Example:
            >>> nearestmin_validPoint(3, 4, [[1,2],[3,1],[2,4],[2,3],[4,4]])
            2

        Time Complexity: O(n), where n is the number of points.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        min_valid = -1
        manh_dist = 10**5

        for i, p in enumerate(points):
            if p[0] == x or p[1] == y:
                curr_dist = abs(x - p[0]) + abs(y - p[1])
                if curr_dist < manh_dist:
                    manh_dist = curr_dist
                    min_valid = i

        return min_valid
