class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        """
        Assuming Alice and Bob play optimally, return True if Alice wins, or
        return False if Bob wins.

        There are n pieces arranged in a line, and each piece is colored either
        by 'A' or by 'B'. You are given a string colors of length n where
        colors[i] is the color of the ith piece.

        Alice and Bob are playing a game where they take alternating turns
        removing pieces from the line. In this game, Alice moves first.

            Alice is only allowed to remove a piece colored 'A' if both its
            neighbors are also colored 'A'. She is not allowed to remove pieces
            that are colored 'B'.
            Bob is only allowed to remove a piece colored 'B' if both its
            neighbors are also colored 'B'. He is not allowed to remove pieces
            that are colored 'A'.
            Alice and Bob cannot remove pieces from the edge of the line.
            If a player cannot make a move on their turn, that player loses and
            the other player wins.

        :param str colors: boxes of candies
        :returns bool alice_win: alice could make (bob_moves + 1) moves

        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 98.35%
        """
        moves = {"A": 0, "B": 0}

        curr = ""
        curr_len = 0
        for color in colors:
            if color != curr:
                if curr_len > 2:
                    moves[curr] += curr_len - 2

                curr = color
                curr_len = 1
            else:
                curr_len += 1

        if curr_len > 2:
            moves[curr] += curr_len - 2

        return moves["A"] > moves["B"]
