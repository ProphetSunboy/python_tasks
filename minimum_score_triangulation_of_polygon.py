class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        """
        Given a convex n-sided polygon with integer values assigned to each vertex
        (provided in the list `values` in clockwise order), this method computes
        the minimum possible score of triangulating the polygon.

        A triangulation divides the polygon into n - 2 triangles, where each triangle's
        vertices are original polygon vertices. The score of a triangulation is
        the sum of the products of the values at the vertices of each triangle.

        The goal is to find the triangulation with the minimum total score.

        Args:
            values (List[int]): List of integers representing the values at each vertex of the polygon in clockwise order.

        Returns:
            int: The minimum possible score achievable by triangulating the polygon.

        Example:
            >>> minScoreTriangulation([1,2,3])
            6
            >>> minScoreTriangulation([3,7,4,5])
            144

        Time Complexity: O(n^3), where n is the number of vertices.
        Space Complexity: O(n^2)
        """
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float("inf")
                for k in range(i + 1, j):
                    cost = values[i] * values[j] * values[k]
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + cost)

        return dp[0][n - 1]
