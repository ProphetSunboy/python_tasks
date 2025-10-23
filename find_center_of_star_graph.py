class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        """
        Given an undirected star graph represented by a 2D list of edges,
        return the center node of the star.

        In a star graph:
            - There is one center node connected to every other node.
            - All other nodes have only one connection (to the center).

        Args:
            edges (List[List[int]]):
                A list of edges, where each edge connects two nodes [ui, vi].

        Returns:
            int: The label of the center node.

        Example:
            >>> findCenter([[1,2],[2,3],[4,2]])
            2

        Time Complexity: O(1) (since the center is always shared by the first two edges).
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        d = {}

        for edge in edges:
            for v in edge:
                if d.get(v, 0):
                    return v
                d[v] = 1

        return -1
