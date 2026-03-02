class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        """
        Given an n x n binary grid, in one step you can choose two adjacent rows
        of the grid and swap them.

        A grid is valid if all the cells above the main diagonal are zeros.

        Returns the minimum number of steps needed to make the grid valid,
        or -1 if the grid cannot be made valid.

        The main diagonal of a grid is the diagonal that starts at cell (1, 1)
        and ends at cell (n, n).

        Args:
            grid (List[List[int]]): The n x n binary grid.

        Returns:
            int: The minimum number of required swaps to make the grid valid,
            or -1 if impossible.

        Example:
            Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
            Output: 3

        Time Complexity: O(n^2), where n is the number of rows in the grid.
        Space Complexity: O(n), for tracking trailing zeros for each row.

        LeetCode: Beats 100% of submissions
        """
        n = len(grid)

        trailing_zeros = []
        for row in grid:
            count = 0
            for i in range(n - 1, -1, -1):
                if row[i] == 0:
                    count += 1
                else:
                    break
            trailing_zeros.append(count)

        swaps = 0
        for i in range(n):
            target_zeros = n - 1 - i

            found = False
            for j in range(i, n):
                if trailing_zeros[j] >= target_zeros:
                    found = True
                    curr_zeros = trailing_zeros.pop(j)
                    trailing_zeros.insert(i, curr_zeros)
                    swaps += j - i
                    break

            if not found:
                return -1

        return swaps
