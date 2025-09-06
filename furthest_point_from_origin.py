class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        """
        Given a string `moves` consisting of characters 'L', 'R', and '_', representing
        moves on a number line starting from the origin (0):

        - 'L': move one step to the left
        - 'R': move one step to the right
        - '_': can be used as either a left or right move

        For each '_', you may choose to move left or right.
        Return the maximum possible distance from the origin after all moves.

        Args:
            moves (str): The sequence of moves.

        Returns:
            int: The maximum possible distance from the origin after all moves.

        Example:
            >>> furthestDistanceFromOrigin("L_RL__R")
            5

        Time Complexity: O(n), where n is the length of moves.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        l, r, us = 0, 0, 0

        for move in moves:
            if move == "L":
                l += 1
            elif move == "R":
                r += 1
            else:
                us += 1

        if r > l:
            return r + us - l
        else:
            return l + us - r
