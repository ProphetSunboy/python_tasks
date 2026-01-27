class Solution:
    def minCost(self, n: int, edges: list[list[int]]) -> int:
        """
        Given a directed, weighted graph with n nodes labeled from 0 to n - 1,
        and a list `edges` where edges[i] = [ui, vi, wi] represents a directed
        edge from node ui to node vi with cost wi.

        Each node `ui` has a switch that can be used at most once. When you arrive
        at node `ui` and have not yet used its switch, you may activate it on one
        of its incoming edges vi → ui to reverse that edge (becoming ui → vi),
        and immediately traverse it. The reversal is only valid for that single
        move, and using a reversed edge costs 2 * wi.

        Returns the minimum total cost to travel from node 0 to node n - 1.
        If it is not possible, returns -1.

        Args:
            n (int): Number of nodes.
            edges (List[List[int]]): List of edges, each as [ui, vi, wi].

        Returns:
            int: The minimum total cost to travel from node 0 to node n - 1, or -1
                if it is not possible.

        Example:
            Input: n = 4, edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]
            Output: 5

        Time Complexity: O(E log V).
        Space Complexity: O(V + E).
        """
        adj = defaultdict(list)
        rev_adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            rev_adj[v].append((u, w))

        dist = [[float("inf")] * 2 for _ in range(n)]
        dist[0][0] = 0
        pq = [(0, 0, 0)]

        while pq:
            d, u, used_now = heapq.heappop(pq)

            if d > dist[u][used_now]:
                continue
            if u == n - 1:
                return d

            for v, w in adj[u]:
                if dist[v][0] > d + w:
                    dist[v][0] = d + w
                    heapq.heappush(pq, (dist[v][0], v, 0))

            if used_now == 0:
                for v, w in rev_adj[u]:
                    if dist[v][0] > d + 2 * w:
                        dist[v][0] = d + 2 * w
                        heapq.heappush(pq, (dist[v][0], v, 0))

        return -1
