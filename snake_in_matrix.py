class Solution:
    def finalPositionOfSnake(self, n: int, commands: list[str]) -> int:
        """
        Calculates the final position of a snake moving in an n x n grid, starting from cell 0,
        after executing a sequence of movement commands.

        Each cell in the grid is identified by: grid[i][j] = (i * n) + j.

        The snake starts at the top-left corner (cell 0) and moves according to the commands provided.
        Each command is one of: "UP", "DOWN", "LEFT", "RIGHT".
        It is guaranteed that the snake will not move outside the grid boundaries.

        Args:
            n (int): The size of the grid (n x n).
            commands (List[str]): List of movement commands.

        Returns:
            int: The position of the final cell where the snake ends up.

        Example:
            >>> finalPositionOfSnake(2, ["RIGHT", "DOWN"])
            3

        Time complexity: O(k), where k is the number of commands.
        Space complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        i, j = 0, 0
        moves = {"UP": [0, -1], "DOWN": [0, 1], "LEFT": [-1, 0], "RIGHT": [1, 0]}

        for command in commands:
            move = moves.get(command)
            i += move[1]
            j += move[0]

        return (i * n) + j
