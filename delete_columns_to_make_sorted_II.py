class Solution:
    def minDeletionSize(self, strs):
        """
        Given a list of n strings `strs`, all having the same length, return the
        minimum number of columns that need to be deleted so that the final list
        is in lexicographically non-decreasing order after all deletions are
        applied.

        At each step, you may delete any set of column indices, and for every
        string, remove those characters.
        The goal is to choose as few columns as possible so that, after
        deletions, each string is less than or equal to its successor.

        Args:
            strs (List[str]): List of n strings, each of equal length m.

        Returns:
            int: The minimum number of columns that must be deleted.

        Example:
            Input: strs = ["ca","bb","ac"]
            Output: 1

        Time Complexity: O(n * m), where n is the number of strings and m is their length.
        Space Complexity: O(n).

        LeetCode: Beats 100% of submissions
        """
        n = len(strs)
        m = len(strs[0])

        sorted_pair = [False] * (n - 1)
        deletions = 0

        for col in range(m):
            need_delete = False
            for i in range(n - 1):
                if not sorted_pair[i] and strs[i][col] > strs[i + 1][col]:
                    need_delete = True
                    break

            if need_delete:
                deletions += 1
                continue

            for i in range(n - 1):
                if not sorted_pair[i] and strs[i][col] < strs[i + 1][col]:
                    sorted_pair[i] = True

        return deletions
