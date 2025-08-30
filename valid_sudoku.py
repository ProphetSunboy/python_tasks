class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """
        Determines if a 9x9 Sudoku board is valid according to the following rules:
            - Each row must contain the digits 1-9 without repetition.
            - Each column must contain the digits 1-9 without repetition.
            - Each of the nine 3x3 sub-boxes must contain the digits 1-9 without repetition.
        Only the filled cells need to be validated; empty cells ('.') are ignored.

        Args:
            board (list[list[str]]): A 9x9 grid representing the Sudoku board, where each cell is a digit '1'-'9' or '.'.

        Returns:
            bool: True if the board is valid, False otherwise.

        Example:
            >>> isValidSudoku([
            ...     ["5","3",".",".","7",".",".",".","."],
            ...     ["6",".",".","1","9","5",".",".","."],
            ...     [".","9","8",".",".",".",".","6","."],
            ...     ["8",".",".",".","6",".",".",".","3"],
            ...     ["4",".",".","8",".","3",".",".","1"],
            ...     ["7",".",".",".","2",".",".",".","6"],
            ...     [".","6",".",".",".",".","2","8","."],
            ...     [".",".",".","4","1","9",".",".","5"],
            ...     [".",".",".",".","8",".",".","7","9"]
            ... ])
            True

        Time Complexity: O(1) (since the board size is fixed at 9x9)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[0])):
                if board[i][j].isdigit():
                    if board[i][j] in seen:
                        return False
                    else:
                        seen.add(board[i][j])

        for j in range(len(board[0])):
            seen = set()
            for i in range(len(board)):
                if board[i][j].isdigit():
                    if board[i][j] in seen:
                        return False
                    else:
                        seen.add(board[i][j])

        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                seen = set()
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        if board[k][l].isdigit():
                            if board[k][l] in seen:
                                return False
                            else:
                                seen.add(board[k][l])

        return True
