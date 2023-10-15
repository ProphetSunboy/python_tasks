class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        """
        On an 8 x 8 chessboard, there is exactly one white rook 'R' and some
        number of white bishops 'B', black pawns 'p', and empty squares '.'.

        When the rook moves, it chooses one of four cardinal directions (north,
        east, south, or west), then moves in that direction until it chooses to
        stop, reaches the edge of the board, captures a black pawn, or is
        blocked by a white bishop. A rook is considered attacking a pawn if the
        rook can capture the pawn on the rook's turn. The number of available
        captures for the white rook is the number of pawns that the rook is
        attacking.

        Return the number of available captures for the white rook.

        :param list[list[int]] board: 8 x 8 chessboard with exactly one white
        rook 'R' and some number of white bishops 'B', black pawns 'p', and
        empty squares '.'
        :returns int captures: number of available captures for the white rook

        Time complexity: O(n^2)
        Space complexity: O(1)

        LeetCode: Beats 97.89%
        """

        def available_captures(k, l):
            captures = 0

            for i in range(k - 1, -1, -1):
                if board[i][l] != ".":
                    if board[i][l] == "p":
                        captures += 1

                    break

            for i in range(k + 1, len(board)):
                if board[i][l] != ".":
                    if board[i][l] == "p":
                        captures += 1

                    break

            for j in range(l - 1, -1, -1):
                if board[k][j] != ".":
                    if board[k][j] == "p":
                        captures += 1

                    break

            for j in range(l + 1, len(board[0])):
                if board[k][j] != ".":
                    if board[k][j] == "p":
                        captures += 1

                    break

            return captures

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "R":
                    return available_captures(i, j)
