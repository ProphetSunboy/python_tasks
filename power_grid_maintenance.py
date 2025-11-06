from collections import defaultdict
import heapq


class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1


class Solution:
    def processQueries(
        self, c: int, connections: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        """
        Processes maintenance and operational queries on a power grid of c stations.

        Behavior:
            - All stations are initially online.
            - Going offline does not affect the network's structure or connectivity.
            - Only queries of type [1, x] produce results to include in the returned list.

        Args:
            c (int): Number of power stations, labeled from 1 to c (inclusive).
            connections (List[List[int]]): Each element [ui, vi] represents a
            bidirectional cable between stations ui and vi. Stations directly or
            indirectly connected belong to the same power grid.
            queries (List[List[int]]): A list of queries. Each query is of two types:
                - [1, x]: Maintenance check for station x. If x is online, return x;
                if offline, return the smallest-id operational station in the
                same grid as x; if none, return -1.
                - [2, x]: Station x goes offline (becomes non-operational).

        Returns:
            List[int]: Results of each maintenance check ([1, x]) in query order.

        Time Complexity: Dependent on queries and grid size.
        - DSU setup: O(c + len(connections) * α(c)), where α is the inverse Ackermann function.
        - Each query:
            - [1, x]: O(log m) (heappop and check), where m is grid size.
            - [2, x]: O(1) removal from set.
        # Space Complexity: O(c) for DSU, heaps, and sets.
        """
        dsu = DSU(c)

        for u, v in connections:
            dsu.union(u, v)

        grids = defaultdict(list)
        for station in range(1, c + 1):
            root = dsu.find(station)
            grids[root].append(station)

        online_heaps = {}
        online_sets = {}
        for root, stations in grids.items():
            heapq.heapify(stations)
            online_heaps[root] = stations[:]
            online_sets[root] = set(stations)

        results = []

        for typ, x in queries:
            root = dsu.find(x)

            if typ == 1:
                if x in online_sets[root]:
                    results.append(x)
                else:
                    while (
                        online_heaps[root]
                        and online_heaps[root][0] not in online_sets[root]
                    ):
                        heapq.heappop(online_heaps[root])

                    if online_heaps[root]:
                        results.append(online_heaps[root][0])
                    else:
                        results.append(-1)

            else:
                if x in online_sets[root]:
                    online_sets[root].remove(x)

        return results
