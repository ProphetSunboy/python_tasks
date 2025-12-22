class Solution:
    def minDeletionSize(self, strs):
        """
        Given a list of n strings `strs`, all of the same length, compute the
        minimum number of columns to delete so that each row is in
        non-decreasing (lexicographic) order after deletions.

        You may delete any subset of columns (deletion indices). After deleting
        these columns from all strings, every string (row) should become
        sorted (i.e., for every row, characters are in non-decreasing order
        from left to right).

        For example:
            Input: strs = ["abcdef", "uvwxyz"], deletion indices = {0, 2, 3}
            After deletions: ["bef", "vyz"]

        The goal is to minimize the number of deletions required so that each
        final row is sorted.

        Args:
            strs (List[str]): A list of strings, all of the same length.

        Returns:
            int: The minimum number of columns that must be deleted.

        Example:
            Input: strs = ["abcdef", "uvwxyz"]
            Output: 3
            Explanation: deletion indices = {0, 2, 3}, after deletions: ["bef", "vyz"]

        Time Complexity: O(m^2 * n), where m is the length of each string and n is the number of strings.
        Space Complexity: O(m).

        LeetCode: Beats 93.33% of submissions
        """
        n = len(strs)
        m = len(strs[0])

        dp = [1] * m

        for j in range(m):
            for i in range(j):
                ok = True
                for r in range(n):
                    if strs[r][i] > strs[r][j]:
                        ok = False
                        break
                if ok:
                    dp[j] = max(dp[j], dp[i] + 1)

        return m - max(dp)
