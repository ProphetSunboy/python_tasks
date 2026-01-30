from typing import List


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        """
        Given two 0-indexed strings, `source` and `target`, each of length n and consisting
        of lowercase English characters, along with two string lists, `original` and
        `changed`, and an integer list `cost` where cost[i] represents the cost of
        converting `original[i]` to `changed[i]`:

        - You start from the string `source`.
        - In one operation, you may select a substring x of the string and change it to y
          at a cost z, provided there is an index j such that cost[j] == z,
          original[j] == x, and changed[j] == y.
        - Any number of operations may be performed, but for any pair of operations,
          the affected substrings must be either disjoint or identical.

        There can exist indices i, j such that original[j] == original[i] and
        changed[j] == changed[i].

        Returns the minimum total cost required to convert `source` to `target` using any
        number of valid operations. If the conversion is not possible, returns -1.

        Args:
            source (str): The starting string to be converted.
            target (str): The target string after conversion.
            original (List[str]): List of substrings that can be replaced.
            changed (List[str]): List of substrings that original can be changed into.
            cost (List[int]): List of costs for each transformation.

        Returns:
            int: The minimum total cost required to convert `source` to `target` using the allowed operations.
                 Returns -1 if the conversion is not possible.

        Example:
            Input: source = "abcd", target = "acbe",
            original = ["a","b","c","c","e","d"],
            changed = ["b","c","b","e","b","e"],
            cost = [2,5,5,1,2,20]
            Output: 28

        Time Complexity: O(M^3 + N * L * max_len), where M is the number of
        unique strings, N is the length of source, L is the number of unique
        substring lengths, and max_len is the maximum length of the substrings.
        Space Complexity: O(M^2 * N), where M^2 is required to store the
        distance matrix for M unique strings and N is for the DP list.
        """
        n = len(source)

        nodes = list(set(original) | set(changed))
        node_to_idx = {s: i for i, s in enumerate(nodes)}
        m = len(nodes)

        dist = [[float("inf")] * m for _ in range(m)]
        for i in range(m):
            dist[i][i] = 0

        for u, v, c in zip(original, changed, cost):
            u_idx, v_idx = node_to_idx[u], node_to_idx[v]
            dist[u_idx][v_idx] = min(dist[u_idx][v_idx], c)

        for k in range(m):
            for i in range(m):
                for j in range(m):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        possible_conversions = []
        conversions_by_len = {}
        for u_idx in range(m):
            for v_idx in range(m):
                if dist[u_idx][v_idx] != float("inf"):
                    u_str, v_str = nodes[u_idx], nodes[v_idx]
                    if len(u_str) == len(v_str):
                        l = len(u_str)
                        if l not in conversions_by_len:
                            conversions_by_len[l] = []
                        conversions_by_len[l].append((u_str, v_idx, dist[u_idx][v_idx]))

        dp = [float("inf")] * (n + 1)
        dp[n] = 0

        lengths = sorted(conversions_by_len.keys())

        for i in range(n - 1, -1, -1):
            if source[i] == target[i]:
                dp[i] = dp[i + 1]

            for l in lengths:
                if i + l > n:
                    break

                sub_source = source[i : i + l]
                sub_target = target[i : i + l]

                if sub_source in node_to_idx:
                    u_idx = node_to_idx[sub_source]
                    if sub_target in node_to_idx:
                        v_idx = node_to_idx[sub_target]
                        cost_val = dist[u_idx][v_idx]
                        if cost_val != float("inf"):
                            dp[i] = min(dp[i], cost_val + dp[i + l])

        return dp[0] if dp[0] != float("inf") else -1
