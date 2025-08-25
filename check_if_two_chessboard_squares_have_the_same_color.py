class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        """
        Determines if two squares on a standard 8x8 chessboard have the same color.

        Each coordinate is a string (e.g., "a1", "h8") representing a square.

        Args:
            coordinate1 (str): The first square's coordinate.
            coordinate2 (str): The second square's coordinate.

        Returns:
            bool: True if both squares have the same color, False otherwise.

        Example:
            >>> checkTwoChessboards("a1", "c3")
            True
            >>> checkTwoChessboards("a1", "h3")
            False

        Time Complexity: O(1)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        if ord(coordinate1[0]) % 2 == ord(coordinate2[0]) % 2:
            return int(coordinate1[1]) % 2 == int(coordinate2[1]) % 2
        else:
            return int(coordinate1[1]) % 2 != int(coordinate2[1]) % 2
