class Solution:
    def pyramidTransition(self, bottom, allowed):
        """
        Determines if a pyramid can be built from a given bottom row of colored blocks
        using only allowed triangular patterns.

        Each block is represented by a single letter. Each row above has one less block,
        and any pair of adjacent blocks can be covered by a block according to the
        'allowed' patterns.

        Each allowed pattern is a string of three characters:
          - The first two characters represent the left and right blocks in a row (base).
          - The third character represents the block that can be placed above that pair.

        For example, "ABC" means a 'C' block can be placed on top of 'A' and 'B'.

        Args:
            bottom (str): The string representing the bottom row of blocks.
            allowed (List[str]): The list of allowed string patterns.

        Returns:
            bool: True if the pyramid can be built to the top (one block), False otherwise.

        Example:
            Input: bottom = "BCD", allowed = ["BCC","CDE","CEA","DEF"]
            Output: True

        Time Complexity: O(3^n), where n is the length of the bottom row.
        Space Complexity: O(3^n), due to memoization of intermediate states.
        """
        from collections import defaultdict

        trans = defaultdict(list)
        for a in allowed:
            trans[(a[0], a[1])].append(a[2])

        memo = {}

        def dfs(row):
            if row in memo:
                return memo[row]

            if len(row) == 1:
                return True

            next_rows = []

            def build(i, curr):
                if i == len(row) - 1:
                    next_rows.append(curr)
                    return

                pair = (row[i], row[i + 1])
                if pair not in trans:
                    return

                for c in trans[pair]:
                    build(i + 1, curr + c)

            build(0, "")

            for nr in next_rows:
                if dfs(nr):
                    memo[row] = True
                    return True

            memo[row] = False
            return False

        return dfs(bottom)
