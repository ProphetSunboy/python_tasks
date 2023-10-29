class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        cols = {i: 1 for i in range(len(strs[0]))}

        for i in range(1, len(strs)):
            a = list(cols.keys())
            for col in a:
                if strs[i][col] < strs[i - 1][col]:
                    cols.pop(col)

        return len(strs[0]) - len(cols)
