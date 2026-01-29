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
        Given two strings source and target consisting of English letters, and two
        0-indexed character lists original and changed, and an integer list cost,
        where cost[i] represents the cost of changing the character original[i] to
        the character changed[i]:

        In one operation, you can pick a character x from source and change it to
        character y at cost z if there exists any index j such that
        original[j] == x, changed[j] == y, and cost[j] == z.

        Returns the minimum cost to convert source to target using any number of
        operations. If it is impossible to convert source to target, returns -1.

        Args:
            source (str): The initial string.
            target (str): The desired target string.
            original (List[str]): List of original characters (length m).
            changed (List[str]): List of characters to change to (length m).
            cost (List[int]): List of costs for each conversion (length m).

        Returns:
            int: The minimum cost to convert source to target, or -1 if impossible.

        Example:
            Input: source = "abcd", target = "acbe",
                original = ["a","b","c","c","e","d"],
                changed = ["b","c","b","e","b","e"],
                cost = [2,5,5,1,2,20]
            Output: 28

        Time Complexity: O(n + k^3), where n is the length of source/target,
        and k is the alphabet size (26).
        Space Complexity: O(k^2), for storing conversion costs between characters.
        """
        dist = [[float("inf")] * 26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0

        for o, c, z in zip(original, changed, cost):
            u, v = ord(o) - ord("a"), ord(c) - ord("a")
            dist[u][v] = min(dist[u][v], z)

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        total_cost = 0
        for s, t in zip(source, target):
            if s != t:
                res = dist[ord(s) - ord("a")][ord(t) - ord("a")]
                if res == float("inf"):
                    return -1
                total_cost += res

        return total_cost
