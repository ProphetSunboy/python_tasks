class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        """
        Determines the number of winning players in a ball-picking game.

        Each player is identified by an integer from 0 to n-1. The 2D list `pick` contains entries [xi, yi],
        indicating that player xi picked a ball of color yi.

        A player i wins if they pick strictly more than i balls of the same color
        (i.e., at least i+1 balls of any single color).

        Args:
            n (int): The number of players.
            pick (List[List[int]]): A list of [player, color] pairs representing each pick.

        Returns:
            int: The number of players who win the game.

        Example:
            >>> winningPlayerCount(3, [[0,1],[1,2],[1,2],[2,3],[2,3],[2,0]])
            2

        Time Complexity: O(m), where m is the number of picks in `pick`.
        Space Complexity: O(n * c), where c is the number of possible colors.

        LeetCode: Beats 100% of submissions
        """
        players = [[0] * 11 for _ in range(n)]

        for p in pick:
            players[p[0]][p[1]] += 1

        winners = 0
        for i, player in enumerate(players):
            if max(player) > i:
                winners += 1

        return winners
