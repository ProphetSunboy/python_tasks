class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        """Determines the winner of a Tic-Tac-Toe game given a sequence of moves.

        The game is played by two players, A ('X') and B ('O'), on a 3x3 grid.
        This function determines the outcome based on a list of moves. A win
        occurs when a player gets three of their characters in a row, column,
        or diagonal. A draw occurs if the board is full with no winner. The
        game is "Pending" if it's not over yet.

        Args:
            moves (list[list[int]]): A list of `[row, col]` positions for each
                                     move in the game. Player A always moves first.

        Returns:
            str: "A" or "B" if a winner is found, "Draw" if the game is a
                 draw, or "Pending" if the game is still in progress.

        Example:
            moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
            # Output: "A"

            moves = [[0,0],[1,1],[0,1],[1,0],[2,2],[0,2],[1,2],[2,1],[2,0]]
            # Output: "Draw"

        LeetCode: Beats 100% of submissions
        """
        players = {0: "X", 1: "O"}
        lines = {
            "f_r": [[0, 0], [0, 1], [0, 2]],
            "s_r": [[1, 0], [1, 1], [1, 2]],
            "t_r": [[2, 0], [2, 1], [2, 2]],
            "f_c": [[0, 0], [1, 0], [2, 0]],
            "s_c": [[0, 1], [1, 1], [2, 1]],
            "t_c": [[0, 2], [1, 2], [2, 2]],
            "d": [[0, 0], [1, 1], [2, 2]],
            "r_d": [[0, 2], [1, 1], [2, 0]],
        }

        for i, move in enumerate(moves):
            for line, val in lines.items():
                for j, v in enumerate(val):
                    if move == v:
                        lines[line][j] = players[i % 2]
                        if val[0] == val[1] == val[2]:
                            return "A" if val[0] == "X" else "B"
                        break

        for line, val in lines.items():
            for v in val:
                if not str(v).isalpha():
                    return "Pending"

        return "Draw"


# Second solution
class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        """
        LeetCode: Beats 100% of submissions
        """
        players = {0: "X", 1: "O"}
        grid = [[0] * 3 for _ in range(3)]

        for i, move in enumerate(moves):
            grid[move[0]][move[1]] = players[i % 2]

        for i in range(3):
            if grid[i][0] != 0 and grid[i][0] == grid[i][1] == grid[i][2]:
                return "A" if grid[i][0] == "X" else "B"

        for j in range(3):
            if grid[0][j] != 0 and grid[0][j] == grid[1][j] == grid[2][j]:
                return "A" if grid[0][j] == "X" else "B"

        if grid[1][1] != 0 and (
            grid[0][0] == grid[1][1] == grid[2][2]
            or grid[0][2] == grid[1][1] == grid[2][0]
        ):
            return "A" if grid[1][1] == "X" else "B"

        if 0 in grid[0] or 0 in grid[1] or 0 in grid[2]:
            return "Pending"

        return "Draw"
