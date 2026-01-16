class Solution:
    def maximizeSquareArea(self, m, n, hFences, vFences):
        """
        Given a (m - 1) x (n - 1) rectangular field with corners at (1, 1) and (m, n),
        containing some horizontal and vertical fences specified by the lists
        hFences and vFences:

        - Horizontal fences extend from (hFences[i], 1) to (hFences[i], n).
        - Vertical fences extend from (1, vFences[i]) to (m, vFences[i]).

        The field is always surrounded by two fixed horizontal fences at
        (1, 1)-(1, n) and (m, 1)-(m, n), and two fixed vertical fences at
        (1, 1)-(m, 1) and (1, n)-(m, n), which cannot be removed.

        Returns the maximum possible area of a square field obtainable by removing
        some (possibly zero) fences. If impossible, returns -1.

        Since the answer may be large, return it modulo 10**9 + 7.

        Args:
            m (int): The number of rows in the field (including boundaries).
            n (int): The number of columns in the field (including boundaries).
            hFences (List[int]): Indices of removable horizontal fences.
            vFences (List[int]): Indices of removable vertical fences.

        Returns:
            int: Maximum area of a square field that can be formed, or -1 if impossible.

        Example:
            Input:
                m = 4, n = 3,
                hFences = [2, 3], vFences = [2]
            Output: 4

        Time Complexity: O(H log H + V log V), where H = len(hFences) and V = len(vFences)
        Space Complexity: O(1), aside from input and output.
        """
        MOD = 10**9 + 7

        h = sorted(hFences + [1, m])
        v = sorted(vFences + [1, n])

        heights = set()
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                heights.add(h[j] - h[i])

        max_side = -1
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                w = v[j] - v[i]
                if w in heights:
                    max_side = max(max_side, w)

        if max_side == -1:
            return -1

        return (max_side * max_side) % MOD
