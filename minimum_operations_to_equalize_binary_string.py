class Solution:
    def minOperations(self, s: str, k: int) -> int:
        """
        Given a binary string s and an integer k, return the minimum number of
        operations required to make all characters in s equal to '1'.
        If it is not possible to do so, return -1.

        In one operation, you must choose exactly k distinct indices and flip
        the values at those positions ('0' to '1' and '1' to '0').

        Args:
            s (str): A binary string.
            k (int): The number of indices to flip in each operation.

        Returns:
            int: The minimum number of operations required,
                or -1 if not possible.

        Example:
            Input: s = "1010", k = 2
            Output: 1

        Time Complexity: O(n log n), as each of the states is processed once,
        and finding the range using binary search takes logarithmic time.
        Space Complexity: O(n), as we store all possible counts of zeros in the
        adjacency lists and the queue.
        """
        n = len(s)
        start_z = s.count("0")
        if start_z == 0:
            return 0

        next_node = list(range(n + 3))
        adj = [list(range(i, n + 3, 2)) for i in range(2)]

        ptr = [0, 0]

        queue = deque([(start_z, 0)])
        visited = {start_z}

        while queue:
            curr_z, steps = queue.popleft()

            z_min = curr_z + k - 2 * min(k, curr_z)
            z_max = curr_z + k - 2 * max(0, k - (n - curr_z))

            p = z_min % 2
            curr_adj = adj[p]

            import bisect

            idx = bisect.bisect_left(curr_adj, z_min)

            new_idx = idx
            while new_idx < len(curr_adj) and curr_adj[new_idx] <= z_max:
                target_z = curr_adj[new_idx]
                if target_z not in visited:
                    if target_z == 0:
                        return steps + 1
                    visited.add(target_z)
                    queue.append((target_z, steps + 1))

                new_idx += 1

            curr_adj[idx:new_idx] = []

        return -1
