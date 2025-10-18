class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        """
        Calculates the minimum total cutting cost to transport two logs of lengths `n` and `m`
        using three trucks that can each carry a log of maximum length `k`.

        You may cut the logs into pieces, where the cost of cutting a log of length `x`
        into two pieces of lengths `len1` and `len2` (such that `len1 + len2 = x`)
        is `len1 * len2`. The goal is to ensure that no resulting piece is longer than `k`,
        and to minimize the total cutting cost. If no cuts are needed, the cost is 0.

        Args:
            n (int): Length of the first log.
            m (int): Length of the second log.
            k (int): Maximum allowed length for any piece (truck capacity).

        Returns:
            int: The minimum total cost required to distribute the logs onto the trucks.

        Example:
            >>> minCuttingCost(6, 5, 5)
            5

        Time Complexity: O(1)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        cost = 0

        if n > k:
            diff = n - k
            cost += (n - diff) * diff

        if m > k:
            diff = m - k
            cost += (m - diff) * diff

        return cost
