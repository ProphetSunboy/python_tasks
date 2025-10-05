class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        """
        Determines if there is a valid path between two vertices in an undirected graph.

        The graph has n vertices labeled from 0 to n - 1. Edges are given as a list of pairs,
        where each pair [u, v] represents a bi-directional edge between u and v.

        Args:
            n (int): Number of vertices in the graph.
            edges (List[List[int]]): List of edges, where each edge is a list [u, v].
            source (int): The starting vertex.
            destination (int): The target vertex.

        Returns:
            bool: True if there is a valid path from source to destination, False otherwise.

        Example:
            >>> validPath(3, [[0,1],[1,2],[2,0]], 0, 2)
            True

        Time Complexity: O(n + e), where n is the number of vertices and e is the number of edges.
        Space Complexity: O(n)

        LeetCode: Beats 98.55% of submissions
        """
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY

        for u, v in edges:
            union(u, v)

        return find(source) == find(destination)
