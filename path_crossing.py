class Solution:
    def isPathCrossing(self, path: str) -> bool:
        """
        Determines if a given path crosses itself.

        Given a string `path` consisting of the characters 'N', 'S', 'E', and 'W',
        each representing a move north, south, east, or west by one unit from the
        current position on a 2D plane, starting at the origin (0, 0).
        The function returns True if the path crosses itself at any point
        (i.e., if any position is visited more than once), and False otherwise.

        Args:
            path (str): A string representing the sequence of moves.

        Returns:
            bool: True if the path crosses itself, False otherwise.

        Example:
            >>> isPathCrossing("NES")
            False
            >>> isPathCrossing("NESWW")
            True

        Time Complexity: O(n), where n is the length of the path.
        Space Complexity: O(n), for storing visited positions.

        LeetCode: Beats 100% of submissions
        """
        visited = {(0, 0): 1}
        moves = {"N": [0, 1], "S": [0, -1], "E": [1, 0], "W": [-1, 0]}
        curr = [0, 0]

        for move in path:
            curr[0] += moves[move][0]
            curr[1] += moves[move][1]

            if visited.get(tuple(curr), 0):
                return True

            visited[tuple(curr)] = 1

        return False
