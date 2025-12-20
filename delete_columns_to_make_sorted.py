# First solution
class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        cols = {i: 1 for i in range(len(strs[0]))}

        for i in range(1, len(strs)):
            a = list(cols.keys())
            for col in a:
                if strs[i][col] < strs[i - 1][col]:
                    cols.pop(col)

        return len(strs[0]) - len(cols)


# Second solution
class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        """
        Given a list of n strings strs, each of the same length, determine how
        many columns must be deleted so that each column is sorted
        lexicographically from top to bottom.

        A column is unsorted if, in any position, the character in the row below
        is less than the one above it.
        You should count and delete all such columns.

        Args:
            strs (List[str]): A list of strings of equal length.

        Returns:
            int: The number of columns that are not sorted lexicographically
            (i.e., the number of columns to delete).

        Example:
            Input: strs = ["abc", "bce", "cae"]
            Grid view:
                a b c
                b c e
                c a e
            Columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted, while
            column 1 ('b', 'c', 'a') is not (since 'a' < 'c').
            Output: 1

        Time Complexity: O(N * M) where N is the number of strings and M is the
        string length (number of columns).
        Space Complexity: O(1).

        LeetCode: Beats 98.99% of submissions
        """
        ans = 0
        for col in zip(*strs):
            if list(col) != sorted(col):
                ans += 1
        return ans
