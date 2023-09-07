class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """
        Return True if the robot returns to the origin after it finishes all of
        its moves, or False otherwise.

        There is a robot starting at the position (0, 0), the origin, on a 2D
        plane. Given a sequence of its moves, judge if this robot ends up at
        (0, 0) after it completes its moves.

        You are given a string moves that represents the move sequence of the
        robot where moves[i] represents its ith move. Valid moves are
        'R' (right), 'L' (left), 'U' (up), and 'D' (down).

        Note: The way that the robot is "facing" is irrelevant. 'R' will always
        make the robot move to the right once, 'L' will always make it move
        left, etc. Also, assume that the magnitude of the robot's movement is
        the same for each move.


        :param str moves: robot movement sequence
        :returns bool returns_to_origin: does the robot returns to origin

        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 96.53%
        """
        c = collections.Counter(moves)

        return c["U"] == c["D"] and c["L"] == c["R"]
