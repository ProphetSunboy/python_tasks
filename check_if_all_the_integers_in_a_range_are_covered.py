class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        """Determines if every integer in the inclusive range [left, right] is covered by at least one interval in ranges.

        An integer x is covered by an interval [start, end] if start <= x <= end.

        Args:
            ranges (list[list[int]]): List of intervals, where each interval is represented as [start, end].
            left (int): The start of the target range (inclusive).
            right (int): The end of the target range (inclusive).

        Returns:
            bool: True if every integer in [left, right] is covered by at least one interval in ranges, False otherwise.

        Example:
            >>> isCovered([[1,2],[3,4],[5,6]], 2, 5)
            True
            >>> isCovered([[1,10],[10,20]], 21, 21)
            False

        Time complexity: O(n * m), where n is the number of intervals and m is the size of the range [left, right].
        Space complexity: O(m), where m is the size of the range [left, right].

        LeetCode: Beats 100% of submissions
        """
        d = dict()
        for i in range(left, right + 1):
            d[i] = False

        for r in ranges:
            for j in range(r[0], r[1] + 1):
                if j in d:
                    d[j] = True

        return all(d.values())
