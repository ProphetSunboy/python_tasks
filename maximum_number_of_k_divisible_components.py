class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    ) -> int:
        """
        Given an undirected tree with n nodes labeled from 0 to n - 1, edges
        describing the connections, a list of node values, and an integer k,
        this function finds the maximum number of components obtainable by
        removing any set of edges (including none) so that the sum of values in
        each connected component is divisible by k.

        Args:
            n (int): The number of nodes in the tree.
            edges (List[List[int]]): A list of edges, where each edge connects two nodes.
            values (List[int]): Values associated with each node.
            k (int): The divisor for component sums.

        Returns:
            int: The maximum number of components where each component's sum of
            node values is divisible by k.

        Example:
            Input:
                n = 5
                edges = [[0,2],[1,2],[1,3],[2,4]]
                values = [1,8,1,4,4]
                k = 6
            Output: 2

        Time Complexity: O(n), where n is the number of nodes.
        Space Complexity: O(n), for adjacency lists and recursion stack.
        """
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        result = 0

        def dfs(node, parent):
            nonlocal result
            subtree_sum = values[node]

            for neighbor in adj[node]:
                if neighbor != parent:
                    subtree_sum += dfs(neighbor, node)

            if subtree_sum % k == 0:
                result += 1
                return 0

            return subtree_sum

        dfs(0, -1)

        return result
