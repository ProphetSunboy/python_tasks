class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        """
        Given an integer n representing nodes numbered from 0 to n - 1, and a
        list of edges where edges[i] = [ui, vi, si, musti], computes the
        maximum possible stability of a valid spanning tree with up to k
        upgrades.

        Each edge connects ui and vi (undirected), has a strength si, and musti
        indicates if the edge must be included in the spanning tree
        (1 means it must and cannot be upgraded; 0 means it may be used and can
        be upgraded at most once if not must-edge).

        Each upgrade doubles the strength of an eligible edge. The stability of
        a spanning tree is the minimum strength among all included edges.
        Return the maximum achievable stability, or -1 if it is impossible to
        span all nodes.

        Args:
            n (int): The number of nodes.
            edges (List[List[int]]): Each element is [ui, vi, si, musti].
            k (int): Maximum number of allowed upgrades.

        Returns:
            int: The maximum possible stability, or -1 if spanning is impossible.

        Example:
            Input: n = 3, edges = [[0,1,2,1],[1,2,3,0]], k = 1
            Output: 2

        Time Complexity: O(E * log(S)), where E is the number of edges,
                and S is the range of strengths.
        Space Complexity: O(E + n), accounting for edge and parent storage.
        """
        parent = list(range(n))

        def find(i, p):
            if p[i] == i:
                return i
            p[i] = find(p[i], p)
            return p[i]

        def union(i, j, p):
            root_i, root_j = find(i, p), find(j, p)
            if root_i != root_j:
                p[root_i] = root_j
                return True
            return False

        must_edges = [e for e in edges if e[3] == 1]
        if len(must_edges) >= n:
            return -1

        temp_p = list(range(n))
        for u, v, s, m in must_edges:
            if not union(u, v, temp_p):
                return -1

        def can_form(mid):
            p = list(range(n))
            count = 0
            for u, v, s, m in must_edges:
                if s < mid:
                    return False
                union(u, v, p)
                count += 1

            for u, v, s, m in edges:
                if m == 0 and s >= mid:
                    if union(u, v, p):
                        count += 1

            upgrades = 0
            if upgrades < k:
                for u, v, s, m in edges:
                    if m == 0 and s < mid and s * 2 >= mid:
                        if upgrades < k and union(u, v, p):
                            count += 1
                            upgrades += 1

            return count == n - 1

        low, high = 0, 2 * 10**9
        res = -1
        while low <= high:
            mid = (low + high) // 2
            if can_form(mid):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res
