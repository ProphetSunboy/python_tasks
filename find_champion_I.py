class Solution:
    def findChampion(self, grid: list[list[int]]) -> int:
        """Determines the champion team in a tournament.

        There are n teams numbered from 0 to n - 1. The tournament results are given
        as a 0-indexed 2D boolean matrix `grid` of size n x n, where for all i ≠ j:
            - grid[i][j] == 1 means team i is stronger than team j,
            - grid[i][j] == 0 means team j is stronger than team i.

        A team a is the champion if there is no team b that is stronger than team a.

        Args:
            grid (list[list[int]]): 2D list representing the results of matches between teams.

        Returns:
            int: The index of the champion team.

        Example:
            >>> findChampion([[0,1,1],[0,0,1],[0,0,0]])
            0

        Time complexity: O(n^2), where n is the number of teams.
        Space complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        winner = 0
        winner_score = 0

        for i, team in enumerate(grid):
            team_score = sum(team)

            if team_score > winner_score:
                winner = i
                winner_score = team_score

        return winner
